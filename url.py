#!/usr/bin.env python
#-*- coding=utf-8 -*-
'''  神秘肉洞 url 结构  '''
from fan.fanfou import directmsg, sendtext, sendphoto
from xml    import xmlmsg
from weixin.wechat import wechatmsg

urls  = ('/wechat  ','wechatmsg',
       '/dm_fetch  ','directmsg',
       '/xml_fetch ','xmlmsg   ',
       '/text_sent ','sendtext ',
       '/photo_sent','sendphoto')
