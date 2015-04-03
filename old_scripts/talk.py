#!/usr/bin/env python
#-*- coding=utf-8 -*-

import urllib
import MySQLdb
import chardet
import hanzi

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_string(wechat):
    conn=MySQLdb.connect(host='localhost',db='fanfou',user='root',passwd='password',charset='utf8')
    cursor=conn.cursor()
    cursor.execute('select num from timeline where wechat=%s',(wechat,))
    start = cursor.fetchone()
    start = start[0]
    cursor.execute('select content from fanfou where id>%s limit 10',(start,))
    talk  = cursor.fetchall()
    string= ''
    if len(talk):
        send_num = 0
        for i in talk:
            string+=i[0]
            string+='\n \n'
            send_num=send_num+1
        num = start+send_num
        cursor.execute('update timeline set num=%s where wechat=%s',(num,wechat))
        conn.commit()
    else:
        string=hanzi.rdall.decode('utf-8')
    cursor.close()
    conn.close()
    return string.encode('utf-8')
