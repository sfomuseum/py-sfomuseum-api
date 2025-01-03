# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
import json
from sfomuseum.api.client import OAuth2Client

def main_function():

    parser = argparse.ArgumentParser(description="Accept multiple key-value pairs.")
    
    parser.add_argument(
        "--access-token",
        action="store",
        default="",
        help="A valid SFO Museum API access token."
        )
    
    parser.add_argument(
        "--verb",
        action="store",
        default="GET",
        help="The HTTP verb used to execute the request."
        )
    
    parser.add_argument(
        "--param",
        action="append",
        help="Specify a key-value pair (e.g., --param key1=value1). Can be used multiple times.",
    )
    
    args = parser.parse_args()
    
    kwargs = {}
    
    if args.param:
        for pair in args.param:
            try:
                key, value = pair.split("=", 1)  # Split on the first "="
                kwargs[key] = value
            except ValueError:
                parser.error(f"Invalid key-value pair: '{pair}'. Expected format is key=value.")
    
    cl = OAuth2Client(args.access_token)
    rsp = cl.execute_method(args.verb, kwargs)

    print(json.dumps(rsp))

    
