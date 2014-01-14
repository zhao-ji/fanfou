#!/usr/bin/env python
#-*- coding=utf-8 -*-

import sys, urllib, urllib2, re ,httplib
import oauth.oauth as oauth
import time
import uuid
import hmac
import time
import hashlib
import binascii
import urlparse

consumer_key       = "9eab891a46e90644738442f4c03d461b"
consumer_secret    = "acce8a65db9d239e8ba5d9865ac6a1d6"
oauth_token_key    = "1436156-3139ae61a2a46f72254ea00f1fbcfda1"
oauth_token_secret = "706fcb982ed0e5e21de71cf62c176006"
token="oauth_token_secret=706fcb982ed0e5e21de71cf62c176006&oauth_token=1436156-3139ae61a2a46f72254ea00f1fbcfda1"

signature_method   = oauth.OAuthSignatureMethod_HMAC_SHA1()
consumer           = oauth.OAuthConsumer(consumer_key, consumer_secret)
oauth_token        = oauth.OAuthToken(oauth_token_key, oauth_token_secret)

def request_to_header(request, realm=''):
    """Serialize as a header for an HTTPAuth request."""
    #auth_header = 'OAuth realm="%s"' % realm
    auth_header = 'OAuth realm="%s"' % realm
        # Add the oauth parameters.
    if request.parameters:
        for k, v in request.parameters.iteritems():
            if k.startswith('oauth_') or k.startswith('x_auth_'):
                auth_header += ', %s="%s"' % (k, oauth.escape(str(v)))
    return {'Authorization': auth_header}
    
def  get(url, **args):
    url  = 'http://api.fanfou.com/%s.xml' %url
    query = args
    request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                     token=oauth_token,
                                                     http_method='GET',
                                                     http_url=url,
                                                     parameters=query)
    request.sign_request(signature_method, consumer, oauth_token)
    headers=request_to_header(request)
    headers.update(query)
    print headers
    req  = urllib2.Request(url, headers=headers)
    try:
        result    = urllib2.urlopen(req)
    except Exception,e:
        print e 
        return 
    code, xml = result.getcode(), result.read()
    print code,xml
    
def post(url, **args):
    url  = 'http://api.fanfou.com/' + url + '.xml'
    all_args = {}
    all_args.update(args)
    base_args = dict(
            oauth_consumer_key     = consumer_key,
            oauth_token            = oauth_token_key,
            oauth_signature_method = "HMAC-SHA1",
            oauth_timestamp        = str(int(time.time())),
            oauth_nonce            = binascii.b2a_hex(uuid.uuid4().bytes),
            oauth_version          = "1.0a", 
        )
    args1 = {}
    args1.update(base_args)
    args1.update(all_args)
    parts = urlparse.urlparse(url)
    scheme, netloc, path = parts[:3]
    normalized_url = scheme.lower() + "://" + netloc.lower() + path

    base_elems = []
    base_elems.append('GET')
    base_elems.append(normalized_url)
    base_elems.append("&".join("%s=%s" % (k, str(v))
                               for k, v in sorted(args.items())))
    
    base_string =  "&".join(e for e in base_elems)
    key_elems = [urllib.quote(consumer_secret, safe='~')]
    key_elems.append(urllib.quote(oauth_token_secret, safe='~') if token else "")
    key = ("&").join(key_elems)

    hash = hmac.new(key, base_string, hashlib.sha1)
    signature = binascii.b2a_base64(hash.digest())[:-1]
    base_args["oauth_signature"] = signature
    args1.update(base_args)
    data = {}
    data.update(args)
    data = urllib.urlencode(data)
    req  = urllib2.Request(url, data=data, headers=args1)
    result    = urllib2.urlopen(req)
    code, xml = result.getcode(), result.read()
    print code,xml
    
if __name__ == '__main__':
    get('direct_messages/inbox',count=1)
