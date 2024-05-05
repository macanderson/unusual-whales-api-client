# unusual-whales-api-client
A client library for accessing Unusual Whales API

Thank you @unusualwhales for providing an excellent api and for leaving your openapi schema unobfuscated from the network logs on your api documentation website :->)

For feature requests email mac@macanderson.com - I do not provide support

## Importing Modules
You can import modules using the following syntax:

from unusualwhales.client import Client
from unusualwhales.api.[tag] import [function]
from unusualwhales.models import [ModelNameHere]
from unusualwhales.types import Response

```python
import os
from dotenv import load_dotenv
from unusualwhales.client import AuthenticatedClient
from unusualwhales.api.[tag] import [function]
from unusualwhales.models import [ModelNameHere]
from unusualwhales.types import Response

load_dotenv('/path/to/.env')
# This app requires an api token to included when initializing a new AuthenticatedClient
# you can use python-dotenv as shown here to save it in a .env file so that you
# do not have unsecured code
API_TOKEN = os.environ.get("UNUSUAL_WHALES_API_TOKEN", None)

client = AuthenticatedClient(base_url="https://api.unusualwhales.com", token=API_TOKEN)
```


```python
import os

from dotenv import load_dotenv

from unusualwhales.client import AuthenticatedClient
from unusualwhales.models import TickerOptionsVolume
from unusualwhales.api.stock import getTickerOptionsVolume
from unusualwhales.types import Response

load_dotenv('/path/to/.env')
API_TOKEN = os.environ.get("UNUSUAL_WHALES_API_TOKEN", None)

client = AuthenticatedClient(base_url="https://api.unusualwhales.com", token=API_TOKEN)
with client as client:
    ticker_options_volume: Response[TickerOptionsVolume] = getTickerOptionsVolume.sync(client=client,ticker="AAPL",date="2024-05-03")
    for option_volume in ticker_options_volume:
        print(option_volume.strike, option_volume.volume)
```

## Async Support

This library works with async await to handle non blocking i/o for better performance!

```python
# same code as before but with async/await note that the function changes from sync_detailed to asyncio_detailed
# alternatively you can use sync and asyncio
from unusualwhales.client import AuthenticatedClient

async with client as client:
    ticker_options_volume: TickerOptionsVolume = await getTickerOptionsVolume.asyncio(client=client,ticker="AAPL",date="2024-05-03")
    for option_volume in ticker_options_volume:
        print(option_volume.strike, option_volume.volume)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from unusual_whales_api_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.unusualwhales.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)
```
