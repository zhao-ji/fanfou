#!/usr/bin/env python
#-*- coding=utf-8 -*-

import sys, urllib, re
import oauth.oauth as oauth
from urllib2 import Request, urlopen

consumer_key = '9eab891a46e90644738442f4c03d461b'   # api key
consumer_secret = 'acce8a65db9d239e8ba5d9865ac6a1d6'  # api secret
access_token_url = 'http://fanfou.com/oauth/access_token'
url_start = 'http://api.fanfou.com/'
url_end = '.xml'

def request_to_header(request, realm=''):
    """Serialize as a header for an HTTPAuth request."""
    auth_header = 'OAuth realm="%s"' % realm
        # Add the oauth parameters.
    if request.parameters:
        for k, v in request.parameters.iteritems():
            if k.startswith('oauth_') or k.startswith('x_auth_'):
                auth_header += ', %s="%s"' % (k, oauth.escape(str(v)))
    return {'Authorization': auth_header}

consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)
params = {}
params["x_auth_username"] = 'daojunhuangdi@gmail.com'
params["x_auth_password"] = 'sfjnz6Wayol'
params["x_auth_mode"] = 'client_auth'
request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                     http_url=access_token_url,
                                                     parameters=params)

signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
request.sign_request(signature_method, consumer, None)
headers=request_to_header(request)

resp = urlopen(Request(access_token_url, headers=headers))
token = resp.read()

m = re.match(r'oauth_token=(?P<key>[^&]+)&oauth_token_secret=(?P<secret>[^&]+)', token)

def get_oauth_token():
    if m:
        oauth_token = oauth.OAuthToken(m.group('key'), m.group('secret'))
        print oauth_token

if __name__ == '__main__':
    get_oauth_token()
