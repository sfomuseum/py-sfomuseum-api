import urllib
from urllib.parse import urlparse
import http.client
import json
import logging

class OAuth2Client:

    def __init__(self, access_token, hostname="api.sfomuseum.org", endpoint="/rest"):

        self.access_token = access_token

        self.hostname = hostname
        self.endpoint = endpoint

        logging.debug("setup API to use %s%s" % (self.hostname, self.endpoint))

    def set_auth(self, kwargs):
        kwargs["access_token"] = self.access_token
        
    def execute_method(self, verb, kwargs):

        self.set_auth(kwargs)

        url = self.endpoint
        logging.debug("calling %s" % url)

        conn = http.client.HTTPSConnection(self.hostname)
        
        match verb:
            case "GET":

                query_string = urllib.parse.urlencode(kwargs)
                path = self.endpoint + "?" + query_string

                conn.request("GET", path)

            case "POST":

                body = urllib.parse.urlencode(kwargs)

                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Content-Length": str(len(body))
                }
                
                conn.request("POST", self.endpoint, body=body, headers=headers)
                
            case _:
                raise Exception("Invalid or unsupported verb")

        rsp = conn.getresponse()
        body = rsp.read()

        logging.debug("response is %s" % body)

        try:
            data = json.loads(body)
        except Exception(e):
            logging.error(e)
            raise Exception(e)

        # check status here...
        
        return data

    def execute_method_paginated(self, verb, kwargs, cb):

        while True:
            
            rsp = self.execute_method(verb, kwargs)

            if not cb(rsp):
                logging.warning("execute_method_paginated callback did not return True, halting iteration")
                break

            # this is the old way and is here for backwards
            # compatibility (20170302/thisisaaronland)
            
            if not rsp.has_key('next_query'):

                pages = rsp.get('pages', None)
                page = rsp.get('page', None)

                if page == pages:
                    break

                kwargs['page'] = page + 1
                continue

            # this is the new shiny
            # (20170302/thisisaaronland)
            
            next_query = rsp.get('next_query', None)

            if not next_query:
                break
            
            tmp = urlparse.parse_qs(next_query)

            # sigh...
            
            for k, v in tmp.items():
                kwargs[k] = v[0]

