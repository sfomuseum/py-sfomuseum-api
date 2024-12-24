# py-sfomuseum-api

Python package for working with the SFO Museum API.

## Install

```
$> pip3 install .
```

## Example

```
from sfomuseum.api.client import OAuth2Client
import json

access_token = "SFOMUSEUM_API_ACCESS_TOKEN"
kwargs = { "method": "api.spec.methods" }

cl = OAuth2Client(access_token)
rsp = cl.execute_method("GET", kwargs)

data = json.load(rsp)
print(json.dumps(data))
```

_Error handling omitted for the sake of brevity._

## Design

The core of this package's approach to the SFO Museum API is the `execute_method` method which takes two input variables:

* The HTTP verb used to execute the method
* A dictionary of key-value pairs specific to the SFO Museum API method being invoked (including the method name itself)

This package does not define any specific mappings for individual API responses. In time there may helper methods for unmarshaling API responses in to typed responses but the baseline for all operations will remain: Query parameters sent over HTTP returning an `io.StringIO` instance that is inspected and validated according to the needs and uses of the tools using the SFO Museum API.

## Tools

By default this package installs a command line `sfomuseum-api` for interacting with the SFO Museum API.

### sfomuseum-api

```
$> sfomuseum-api -h
usage: sfomuseum-api [-h] [--access-token ACCESS_TOKEN] [--verb VERB] [--param PARAM]

Accept multiple key-value pairs.

options:
  -h, --help            show this help message and exit
  --access-token ACCESS_TOKEN
                        A valid SFO Museum API access token.
  --verb VERB           The HTTP verb used to execute the request.
  --param PARAM         Specify a key-value pair (e.g., --param key1=value1). Can be used multiple times.
```

For example:

```
$> sfomuseum-api \
	--access-token {SFOMUSEUM_API_ACCESS_TOKEN} \
	--param method=api.spec.methods \
	| jq -r '.methods[]["name"]'
	
sfomuseum.you.shoebox.addObject
sfomuseum.you.shoebox.addFlight
sfomuseum.you.shoebox.addInstagramPost
sfomuseum.you.shoebox.listItems
sfomuseum.you.shoebox.removeItem
sfomuseum.you.shoebox.emptyShoebox
sfomuseum.you.shoebox.typesMap
sfomuseum.millsfield.twitter.getInfo
sfomuseum.millsfield.twitter.getHashTags
sfomuseum.millsfield.twitter.getPostsForHashTag
sfomuseum.millsfield.instagram.getInfo
sfomuseum.millsfield.instagram.getHashTags
... and so on
```

## Creating a SFO Museum API acccess token

The easiest and fastest way to create a SFO Museum API access token is to use the handy [Create a new access token for yourself](https://api.sfomuseum.org/oauth2/authenticate/like-magic/) webpage.

## See also

* https://api.sfomuseum.org/