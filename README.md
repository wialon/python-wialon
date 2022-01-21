AIO Wialon
=========

`AIO Wialon` is an async realisation of Python wrapper for Remote Api, 
forked from https://github.com/wialon/python-wialon. (Now with support for Python 3 since v1.0.2)

Installation
------------
    pip install py-aiowialon

Usage
-----

```python
import asyncio
from aiowialon import Wialon, WialonEvents, flags

is_df = True

def run():
    """
    Poling example
    """

    wialon_session = Wialon(host='TEST HOST', token='TEST TOCKEN')

    @wialon_session.event_handler
    async def df_ev(event: WialonEvents):
        global is_df
        while is_df:
            spec = {
                'itemsType': 'avl_unit',
                'propName': 'sys_name',
                'propValueMask': '*',
                'sortType': 'sys_name'
            }
            interval = {"from": 0, "to": 100}
            units = await wialon_session.core_search_items(spec=spec, force=1, flags=5, **interval)
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
            is_df = False

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

    wialon_session.start_poling()

run()
```

API Documentation
-----------------

[Wialon Remote Api documentation](http://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/apiref "Remote Api")
