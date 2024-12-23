import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sfomuseum.api.client import OAuth2Client

token = ""
cl = OAuth2Client(token)

kwargs = { "method": "api.spec.methods" }

rsp = cl.execute_method("GET", kwargs)

print(rsp)
