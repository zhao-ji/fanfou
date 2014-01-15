#!/usr/bin/env python
#-*- coding=utf-8 -*-

import web
import urllib
import MySQLdb
import chardet
import hanzi

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

db=web.database(dbn='mysql',db='fanfou',user='root',pw='password')

def save(message,source):
    '''
   存储talk或图片地址
   输入 消息和来源
   数据库over字段自动设置为0
          id字段自增
    '''
    
    #message=unicode(message,'utf-8')
    db.insert('fanfou' ,source=source ,over=0 ,content=message)
    
def get_text():
    '''
   获取一条最旧的未发送text
   无输入
   输出id,text
    '''
    item = db.select('fanfou' ,what='id,content' ,limit=1 ,where='over=0 and source<3')
    talk = item[0]
    return talk.id ,talk.content.encode('utf-8')
        
def over(id):
    '''
   将数据库中的消息状态置为已发送
   输入消息id
   无输出
    '''
    db.update('fanfou' ,where='id=$id' ,over=1 ,vars=locals())
    
