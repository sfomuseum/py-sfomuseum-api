# py-sfomuseum-api

## Example

```
from sfomuseum.api.client import OAuth2Client

access_token = "SFOMUSEUM_API_ACCESS_TOKEN"
kwargs = { "method": "api.spec.methods" }

cl = OAuth2Client(access_token)
rsp = cl.execute_method("GET", kwargs)
```