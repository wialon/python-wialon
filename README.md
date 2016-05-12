Wialon
=========

`Wialon` is a Python wrapper for Remote Api. (Now with support for Python 3 since v1.0.2)

Installation
------------
    pip install python-wialon

Usage
-----

```python
from wialon import Wialon, WialonError

try:
    wialon_api = Wialon()
    # old username and password login is deprecated, use token login
    result = wialon_api.token_login(token='YOUR WIALON USER TOKEN')
    wialon_api.sid = result['eid']

    result = wialon_api.avl_evts()

    wialon_api.core_logout()
except WialonError as e:
    pass
```

API Documentation
-----------------

[Wialon Remote Api documentation](http://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/apiref "Remote Api")
