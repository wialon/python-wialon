#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from urllib import urlencode
    from urlparse import urljoin
except Exception:
    from urllib.parse import urlencode, urljoin

try:
    from urllib2 import Request, urlopen, HTTPError, URLError
except ImportError:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError

try:
    import simplejson as json
    assert json  # Silence potential warnings from static analysis tools
except ImportError:
    import json


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
        if (self._code in WialonError.errors):
            explanation = " ".join([WialonError.errors[self._code], self._text])

        message = u'{error} ({code})'.format(error=explanation, code=self._code)
        return u'WialonError({message})'.format(message=message)

    def __str__(self):
        return unicode(self).encode("utf8")

    def __repr__(self):
        return str(self)


class Wialon(object):
    def __init__(self, scheme='http',  host="hst-api.wialon.com", port=80, sid=None, **extra_params):
        """
        Created the Wialon API object.
        """
        self._sid = sid
        self.__default_params = {}
        self.__default_params.update(extra_params)

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

    def update_extra_params(self, **params):
        """
        Updated the Wialon API default parameters.
        """
        self.__default_params.update(params)

    def avl_evts(self):
        """
        Call avl_event request
        """
        url = urljoin(self.__base_url, 'avl_evts')
        params = {
            'sid': self.sid
        }

        return self.request('avl_evts', url, params)

    def call(self, action, *argc, **kwargs):
        """
        Call the API method provided with the parameters supplied.
        """

        if (not kwargs):
            # List params for batch
            params = json.dumps(argc, ensure_ascii=False)
        else:
            params = json.dumps(kwargs, ensure_ascii=False)
        params = {
            'svc': action.replace('_', '/', 1),
            'params': params.encode("utf-8"),
            'sid': self.sid
        }
        all_params = self.__default_params.copy()
        all_params.update(params)
        return self.request(action, self.__base_api_url, all_params)

    def request(self, action, url, params):
        url_params = urlencode(params)
        data = url_params.encode('utf-8')
        try:
            request = Request(url, data)
            response = urlopen(request)
            response_content = response.read()
        except HTTPError as e:
            raise WialonError(0, u"HTTP {code}".format(code=e.code))
        except URLError as e:
            raise WialonError(0, unicode(e))

        content_type = response.info().getheader('Content-Type')
        result = response_content.decode('utf-8', errors='ignore')
        try:
            if content_type == 'application/json':
                result = json.loads(result)
        except ValueError as e:
            raise WialonError(
                0,
                u"Invalid response from Wialon: {0}".format(e),
            )

        if (isinstance(result, dict) and 'error' in result and result['error'] > 0):
            raise WialonError(result['error'], action)

        errors = []
        if isinstance(result, list):
            # Check for batch errors
            for elem in result:
                if (not isinstance(elem, dict)):
                    continue
                if "error" in elem:
                    errors.append("%s (%d)" % (WialonError.errors[elem["error"]], elem["error"]))

        if (errors):
            errors.append(action)
            raise WialonError(0, " ".join(errors))

        return result

    def __getattr__(self, action_name):
        """
        Enable the calling of Wialon API methods through Python method calls
        of the same name.
        """
        def get(self, *args, **kwargs):
            return self.call(action_name, *args, **kwargs)

        return get.__get__(self)

if __name__ == '__main__':
    try:
        wialon_api = Wialon()
        # token/login request
        token = 'TEST TOKEN HERE'
        result = wialon_api.token_login(token=token)
        wialon_api.sid = result['eid']
        # get events
        result = wialon_api.avl_evts()
        # core/logout request
        wialon_api.core_logout()
    except WialonError:
        pass
