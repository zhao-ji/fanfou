#!/usr/bin/env python
# coding=utf-8

import logging
import urllib, urllib2

import api

def save(url, name):
    headers = {}
    headers['User-Agent']      = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:22.0) Gecko/20100101 Firefox/22.0'
    headers['Accept']          = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'
    headers['Accept-Encoding'] = 'gzip, deflate'
    headers['Connection']      = 'keep-alive'

    req = urllib2.Request(url=url,headers=headers)
    get = urllib2.urlopen(req)
    pic = get.read()
    get.close()

    f = file('/home/fanfou/picture/%s.jpg'% name,'w')
    f.write(pic)
    f.close()
    
    pic_stream = file('/home/fanfou/picture/%s.jpg'% name).read()
    code=api.post_photo(pic)
    return code

