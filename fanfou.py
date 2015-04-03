#!/usr/bin/env python
#-*- coding=utf-8 -*-

import string
import time

from lxml import etree

import api

def get_directmsg():
    xml = api.get('direct_messages/inbox')
    if xml:
        xml = etree.fromstring(xml)
        num = len(xml)
        if num > 0:
            for i in range(num):
                id = xml[i][0].text
                msg = xml[i][1].text
                sendtext(content)
                code = api.post('direct_messages/destroy', id=id)
                while code != 1:
                    code, xml = api.fanfou('direct_messages/destroy',{'id':id})

def sendtext(content):
    xml = api.get('account/rate_limit_status')
    xml = etree.fromstring(xml)
    limit_num = xml[1].text
    if string.atoi(limit_num) == 0:
        return
    code = api.post('statuses/update',status=content)

if __name__ == '__main__':
    directmsg()
