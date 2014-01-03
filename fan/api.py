#!/usr/bin/env python
#-*- coding=utf-8 -*-

import sys, urllib, urllib2, re ,httplib
import oauth.oauth as oauth

consumer_key       = "d407ba07ae8902c1e259f9f0166e8b56"
consumer_secret    = "db21de28bf0f763834e40469ffdf64e4"
oauth_token_key    = "1436156-0bbe0a67f4a1ea70f912e50962744738"
oauth_token_secret = "99a903b0c38091412021a1e7d035f6cb"
token="oauth_token_secret=99a903b0c38091412021a1e7d035f6cb&oauth_token=1436156-0bbe0a67f4a1ea70f912e50962744738"

signature_method   = oauth.OAuthSignatureMethod_HMAC_SHA1()
consumer           = oauth.OAuthConsumer(consumer_key, consumer_secret)
oauth_token        = oauth.OAuthToken(oauth_token_key, oauth_token_secret)

def request_to_header(request, realm=''):
    """Serialize as a header for an HTTPAuth request."""
    auth_header = 'OAuth realm="%s"' % realm
        # Add the oauth parameters.
    if request.parameters:
        for k, v in request.parameters.iteritems():
            if k.startswith('oauth_') or k.startswith('x_auth_'):
                auth_header += ', %s="%s"' % (k, oauth.escape(str(v)))
    return {'Authorization': auth_header}
    
def  get(url, **args):
    url  = 'http://api.fanfou.com/' + url + '.xml'
    request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                     token=oauth_token,
                                                     http_method='GET',
                                                     http_url=url,
                                                     parameters=args)
    request.sign_request(signature_method, consumer, oauth_token)
    headers=request_to_header(request)
    headers.update(args)
    req  = urllib2.Request(url,headers=headers)
    try:
        result    = urllib2.urlopen(req)
        code, xml = result.getcode(), result.read()
        return code,xml
    except urllib2.HTTPError:
        print urllib2.HTTPError.info
    
'''def post(url, **args):
    url  = 'http://api.fanfou.com/' + url + '.xml'
    head = {}
    head['Authorization'] = 
    data = {}
    data.update(args)
    data = urllib.urlencode(data)
    req  = urllib2.Request(url, data=data, headers=head)
    result    = urllib2.urlopen(req)
    code, xml = result.getcode(), result.read()
    return code,xml'''
    
