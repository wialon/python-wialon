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
    result = wialon_api.core_login(user='YOUR WIALON USER LOIGN', password='YOUR WIALON USER PASSWORD')
    wialon_api.sid = result['eid']
except WialonError:
    pass
```
    
API Documentation
-----------------

[Wialon Remote Api documentation](http://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/apiref "Remote Api")
