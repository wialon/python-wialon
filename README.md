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
from wialon import Wialon, WialonError

async def main(host, token):
    try:
        wialon_api = Wialon(host=host)
        # token/login request
        result = await wialon_api.token_login(token=token)
        wialon_api.sid = result['eid']

        # avl_evts request
        await wialon_api.avl_evts()

        # core/logout request
        await wialon_api.core_logout()
    except WialonError:
        pass

    
if __name__ == '__main__':
    asyncio.run(main(
        "host",
        "TEST TOKEN HERE"
    ))
```

API Documentation
-----------------

[Wialon Remote Api documentation](http://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/apiref "Remote Api")
