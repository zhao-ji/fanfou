#!/usr/bin/env python
#-*- coding=utf-8 -*-

'''
  消息的数据库操作:存储和提取
'''

import web
import urllib
import MySQLdb
import chardet

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
    if chardet.detect(message)['encoding']=='utf-8':
        message=unicode(message,'utf-8')
    db.insert('fanfou' ,source=source ,over=0 ,content=message)
    
def text_get():
    '''
   获取一条最旧的未发送text
   无输入
   输出id,text
    '''
    item = db.select('fanfou' ,what='id,content' ,limit=1 ,where='over=0 and source<3')
    talk = item[0]
    return talk.id ,talk.content.encode('utf-8')

def photo_get():
    '''
   获取一条最旧的未发送图片
   无输入
   输出talk
    '''
    item = db.select('fanfou' ,what='id,content' ,limit=1 ,where='over=0 and source=3')
    photo= item[0]
    url  = photo.content.encode('utf-8')
    pic  = urllib.urlretrieve(url)
    return photo.id ,pic
        
def over(id):
    '''
   将数据库中的消息状态置为已发送
   输入消息id
   无输出
    '''
    db.update('fanfou' ,where='id=$id' ,over=1 ,vars=locals())    
    
