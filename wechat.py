#!/usr/bin/env python
#-*- coding=utf-8 -*-

import hashlib
import time
import urllib, urllib2

from lxml import etree

import web

from fanfou import sendtext
import hanzi
import photo

render = web.template.render('templates/')

class wechatmsg:
    def GET(self):
        token = "fanfou"
        params = web.input()
        args = [token, params['timestamp'], params['nonce']]
        args.sort()
        if hashlib.sha1("".join(args)).hexdigest() == params['signature']:
            if params.has_key('echostr'):
                return params['echostr']

    def POST(self):
        str_xml = web.data()
        xml     = etree.fromstring(str_xml)
        msgType = xml.find("MsgType").text
        fromUser= xml.find("FromUserName").text
        toUser  = xml.find("ToUserName").text

        if msgType=='event':
            event = xml.find("Event").text
            if event == 'subscribe' :
                return render.weixin(
                    fromUser, toUser, int(time.time()), hanzi.hello)

        elif msgType=='text' :
            content  = xml.find("Content").text
            sendtext(content)
            return render.weixin(fromUser,toUser,int(time.time()),hanzi.txtok)

        elif msgType=='image':
            pic_url  = xml.find("PicUrl").text
            msg_id   = xml.find("MsgId").text
            info     = photo.save(pic_url)
            if info == 1:
                return render.weixin(fromUser,toUser,int(time.time()),hanzi.picok)
            else:
                return render.weixin(fromUser,toUser,int(time.time()),info)

        else:
            return render.weixin(fromUser,toUser,int(time.time()),hanzi.cnfse)
