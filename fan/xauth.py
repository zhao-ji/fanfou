#!/usr/bin/env python
#-*- coding=utf-8 -*-

import sys, urllib, re
import oauth.oauth as oauth
from urllib2 import Request, urlopen

consumer_key = 'd407ba07ae8902c1e259f9f0166e8b56'   # api key
consumer_secret = 'db21de28bf0f763834e40469ffdf64e4'  # api secret
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

def hello():
    if m:
        oauth_token = oauth.OAuthToken(m.group('key'), m.group('secret'))
        return oauth_token

def fanfou(url,data=None):
    if m:
        oauth_token = oauth.OAuthToken(m.group('key'), m.group('secret'))
        request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                     token=oauth_token,
                                                     http_url=url_start+url+url_end)
        request.sign_request(signature_method, consumer, oauth_token)
        headers=request_to_header(request)
        if data==None:
            req  = Request(url_start+url+url_end, headers=headers)
            resp = urlopen(req)
        else:
            data = urllib.urlencode(data)
            req  = Request(url_start+url+url_end, data, headers=headers)
            resp = urlopen(req)
        resp = resp.read()
        print resp 
hello()
