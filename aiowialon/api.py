#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from builtins import str
except:
    str = lambda x: "%s" % x

try:
    import simplejson as json
    assert json  # Silence potential warnings from static analysis tools
except ImportError:
    import json

from urllib.parse import urljoin
import asyncio


try:
    import aiohttp
    from aiohttp.client_exceptions import *
except ImportError:
    import aiohttp

from typing import Callable, Coroutine


class WialonError(Exception):
    """
    Exception raised when an Wialon Remote API call fails due to a network
    related error or for a Wialon specific reason.
    """
    errors = {
        1: 'Invalid session',
        2: 'Invalid service',
        3: 'Invalid result',
        4: 'Invalid input',
        5: 'Error performing request',
        6: 'Unknow error',
        7: 'Access denied',
        8: 'Invalid user name or password',
        9: 'Authorization server is unavailable, please try again later',
        1001: 'No message for selected interval',
        1002: 'Item with such unique property already exists',
        1003: 'Only one request of given time is allowed at the moment'
    }

    def __init__(self, code, text):
        self._text = text
        self._code = code
        try:
            self._code = int(code)
        except ValueError:
            pass

    def __unicode__(self):
        explanation = self._text
        if self._code in WialonError.errors:
            explanation = " ".join([WialonError.errors[self._code], self._text])

        message = u'{error} ({code})'.format(error=explanation, code=self._code)
        return u'WialonError({message})'.format(message=message)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return str(self)


class Wialon(object):
    request_headers = {
        'Accept-Encoding': 'gzip, deflate'
    }

    def __init__(self, scheme='http', host="hst-api.wialon.com", port=80, token=None, sid=None, **extra_params):
        """
        Created the Wialon API object.
        """
        self._sid = sid
        self._token = token
        self.__default_params = {}
        self.__default_params.update(extra_params)
        self.__handlers = []
        self._session_did_open = None

        self.__base_url = (
            '{scheme}://{host}:{port}'.format(
                scheme=scheme,
                host=host,
                port=port
            )
        )

        self.__base_api_url = urljoin(self.__base_url, 'wialon/ajax.html?')

    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value):
        self._sid = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def session_did_open(self, callback: Callable[[None], Coroutine]):
        self._session_did_open = callback

    def update_extra_params(self, **params):
        """
        Updated the Wialon API default parameters.
        """
        self.__default_params.update(params)

    def event_handler(self, callback: object):
        self.__handlers.append(callback)

    def start_poling(self, token=None, timeout=2):
        if token:
            self.token = token
        asyncio.run(self.poling(self.token, timeout))

    async def poling(self, token=None, timeout=2):
        await self.token_login(token=token)
        while self.sid:
            response = await self.avl_evts()
            await asyncio.gather(*[callback(WialonEvents(response)) for callback in self.__handlers])
            await asyncio.sleep(timeout)

    async def avl_evts(self):
        """
        Call avl_event request
        """
        url = urljoin(self.__base_url, 'avl_evts')
        params = {
            'sid': self.sid
        }

        return await self.request('avl_evts', url, params)

    async def call(self, action_name, *argc, **kwargs):
        """
        Call the API method provided with the parameters supplied.
        """

        if not kwargs:
            # List params for batch
            if isinstance(argc, tuple) and len(argc) == 1:
                params = json.dumps(argc[0], ensure_ascii=False)
            else:
                params = json.dumps(argc, ensure_ascii=False)
        else:
            params = json.dumps(kwargs, ensure_ascii=False)

        params = {
            'svc': action_name.replace('_', '/', 1),
            'params': params,
            'sid': self.sid
        }

        all_params = self.__default_params.copy()
        all_params.update(params)
        return await self.request(action_name, self.__base_api_url, all_params)

    async def token_login(self, token=None, *args, **kwargs):
        if token:
            self.token = token
        kwargs['token'] = self.token
        kwargs['appName'] = 'py-aiowialon'
        sess = await self.call('token_login', *args, **kwargs)
        if sess:
            self.sid = sess['eid']
        if self._session_did_open:
            await self._session_did_open()
        return sess

    async def request(self, action_name, url, payload):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=payload, headers=self.request_headers) as response:
                    response_data = await response.read()
                    response_headers = response.headers
                    content_type = response_headers.getone('Content-Type')

                    try:
                        if content_type == 'application/json':
                            result = json.loads(response_data)
                    except ValueError as e:
                        raise WialonError(
                            0,
                            u"Invalid response from Wialon: {0}".format(e),
                        )

                    if isinstance(result, dict) and 'error' in result and result['error'] > 0:
                        raise WialonError(result['error'], action_name)

                    errors = []
                    if isinstance(result, list):
                        # Check for batch errors
                        for elem in result:
                            if not isinstance(elem, dict):
                                continue
                            if "error" in elem:
                                errors.append("%s (%d)" % (WialonError.errors[elem["error"]], elem["error"]))

                    if errors:
                        errors.append(action_name)
                        raise WialonError(0, " ".join(errors))

                    return result
        except ClientResponseError as e:
            raise WialonError(0, u"HTTP {code}".format(e.status))
        except ClientConnectorError as e:
            raise WialonError(0, str(e))

        except Exception as err:
            return err

    def __getattr__(self, action_name):
        """
        Enable the calling of Wialon API methods through Python method calls
        of the same name.
        """
        def get(_self, *args, **kwargs):
            return self.call(action_name, *args, **kwargs)

        return get.__get__(self, object)

    async def core_use_auth_hash(self, *args, **kwargs):
        return await self.call('core_use_auth_hash', *args, *kwargs)


class WialonEvents(object):
    def __init__(self, evts):
        self.__tm = evts['tm']
        self.__events = evts['events']
        self._data = {}
        self.parse_events()

    @property
    def data(self):
        return self._data

    def parse_events(self):
        for e in self.__events:
            self._data[e['i']] = WialonEvent(self.__tm, e)


class WialonEvent(object):
    types = {'m': 'Message', 'u': 'Update', 'd': 'Delete'}

    def __init__(self, tm, e):
        self._tm = tm
        self._e = e
        self._item = e['i']
        self._e_type = self.types[e['t']]
        self._desc = e['d']

    @property
    def item(self):
        return self._item

    @property
    def desc(self):
        return self._desc

    @property
    def e_type(self):
        return self._e_type


if __name__ == '__main__':

    async def main(host, token):
        """
        Example of manual using
        """
        try:
            wialon_api = Wialon(host=host)
            result = await wialon_api.token_login(token=token)
            wialon_api.sid = result['eid']
            await wialon_api.avl_evts()
            await wialon_api.core_logout()
        except WialonError:
            pass


    def run():
        """
        Poling example
        """
        from aiowialon import flags

        wialon_session = Wialon(host='TEST HOST', token='TEST TOKEN')

        async def session_did_open():
            spec = {
                'itemsType': 'avl_unit',
                'propName': 'sys_name',
                'propValueMask': '*',
                'sortType': 'sys_name'
            }
            interval = {"from": 0, "to": 100}
            units = await wialon_session.core_search_items(spec=spec, force=1, flags=5, **interval)
            if 'items' in units:
                ids = [u['id'] for u in units['items']]

                spec = [
                    {
                        "type": "col",
                        "data": ids,
                        "flags": flags.ITEM_DATAFLAG_BASE + flags.ITEM_UNIT_DATAFLAG_POS,
                        "mode": 0
                    }
                ]
                await wialon_session.core_update_data_flags(spec=spec)

        @wialon_session.event_handler
        async def event_handler(events: WialonEvents):
            if 116106 in events.data:
                item_event: WialonEvent = events.data[116106]
                print(item_event.item, item_event.e_type, item_event.desc)

        @wialon_session.event_handler
        async def event_handler(events: WialonEvents):
            spec = {
                'itemsType': 'avl_unit',
                'propName': 'sys_name',
                'propValueMask': '*',
                'sortType': 'sys_name'
            }
            interval = {"from": 0, "to": 0}
            units = await wialon_session.core_search_items(spec=spec, force=1, flags=5, **interval)
            print(events.__dict__, units['totalItemsCount'])

        wialon_session.session_did_open(callback=session_did_open)
        wialon_session.start_poling()

    run()
