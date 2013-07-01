Wialon
=========

`Wialon` is a Python wrapper for Wialon Api. (Now with support for Python 3)

Installation
------------
    pip install python-wialon
    
Usage
-----

```python
from wialon import WialonError

try:
    result = wialon_api.core_login(user='YOUR WIALON USER LOIGN', password='YOUR WIALON USER PASSWORD')
    wialon_api.sid = result['eid']
except WialonError as error:
    print error
```
    
API Documentation
-----------------

[Wialon Remote Api documentation](http://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/apiref "Remote Api")
