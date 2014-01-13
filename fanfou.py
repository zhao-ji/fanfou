#!/usr/bin/env python
#-*- coding=utf-8 -*-

from lxml     import etree
from database import message
from fan      import api

class directmsg:
    def GET(self):
        code,xml = api.fanfou('direct_messages/inbox')
        while code==200:
            xml    = etree.fromstring(xml)
            num    = len(xml)
            for i in range(num):
                id     = xml[i][0].text
                msg    = xml[i][1].text
                message.save(msg,2)
                code,xml = api.fanfou('direct_messages/destroy',{'id':id})
                while code != 200:code,xml = api.fanfou('direct_messages/destroy',{'id':id})

class sendtext:
    def GET(self):
        id,content = message.text_get()
        code,xml = api.fanfou('statuses/update',{'statuses':content})
        while code==200:message.over(id)

class sendphoto:
    def GET(self):
        id,content = message.photo_get()
        code,xml = api.fanfou('photos/uploads',{'statuses':content})
        while code==200:message.over(id)
