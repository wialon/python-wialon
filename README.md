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
from wialon import Wialon, WialonEvent, flags

wialon_api = Wialon(host='host',
                    token='TEST TOKEN HERE')

@wialon_api.event_handler
async def event_handler(event: WialonEvent):
    spec = {
        'itemsType': 'avl_unit',
        'propName': 'sys_name',
        'propValueMask': '*',
        'sortType': 'sys_name'
    }
    interval = {"from": 0, "to": 0}
    units = await wialon_api.core_search_items(spec=spec, force=1, flags=flags.ITEM_DATAFLAG_BASE, **interval)
    print(event.__dict__, units['totalItemsCount'])

wialon_api.start_poling()
```

API Documentation
-----------------

[Wialon Remote Api documentation](http://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/apiref "Remote Api")
