#!/usr/bin/env python
#-*- coding=utf-8 -*-

import web
import hashlib, time, re
import urllib, urllib2
import message
import talk 
import hanzi
import photo
from lxml import etree

render = web.template.render('templates/')
db     = web.database(dbn='mysql',user='root',pw='password',db='fanfou')

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
            if   event == 'subscribe'  :
                count = db.query("select count(id) as num from fanfou") 
                num   = count[0].num - 20
                db.insert('timeline', wechat=fromUser ,num=num)
                return render.weixin(fromUser,toUser,int(time.time()),hanzi.hello)
            elif event == 'unsubscribe':
                db.delete('timeline', where='wechat=$fromUser', vars=locals())
                
        elif msgType=='text' :
            content  = xml.find("Content").text
            if content=="。":
                string = talk.get_string(fromUser)
                return render.weixin(fromUser,toUser,int(time.time()),string)
            else:
                message.save(content,1)
                return render.weixin(fromUser,toUser,int(time.time()),hanzi.txtok)
            
        elif msgType=='image':
            pic_url  = xml.find("PicUrl").text
            msg_id   = xml.find("MsgId").text
            info     = photo.save(msg_id, pic_url)
            if info == 1:
                return render.weixin(fromUser,toUser,int(time.time()),hanzi.cnfse)
            
        else:
            return render.weixin(fromUser,toUser,int(time.time()),hanzi.cnfse)
