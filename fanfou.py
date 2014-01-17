#!/usr/bin/env python
#-*- coding=utf-8 -*-

from lxml import etree
import message
import api
import string
import time

def directmsg():
    xml = api.get('direct_messages/inbox')
    if xml:
        xml    = etree.fromstring(xml)
        num    = len(xml)
        if num>0:
            for i in range(num):
                id     = xml[i][0].text
                msg    = xml[i][1].text
                message.save(msg,2)
                code   = api.post('direct_messages/destroy',id=id)
                while code != 1:code,xml = api.fanfou('direct_messages/destroy',{'id':id})

def sendtext():
    xml        = api.get('account/rate_limit_status')
    xml        = etree.fromstring(xml)
    limit_num  = xml[1].text
    if string.atoi(limit_num) == 0:
        return
    id,content = message.get_text()
    code       = api.post('statuses/update',status=content)
    #if code == 1:
    message.over(id)

if __name__ == '__main__':
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    sendtext()
    time.sleep(3)
    directmsg() 
