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
    conn=MySQLdb.connect(host='localhost',db='fanfou',user='root',passwd='password')
    cursor=conn.cursor()
    cursor.execute('select num from timeline where wechat=%s',(wechat,))
    start = cursor.fetchone()
    start = start[0]
    cursor.execute('select content from fanfou where id>%s limit 10',(start,))
    talk  = cursor.fetchall()
    string= ''
    if talk:
        send_num = 0
        for i in talk:
            string+=i[0].encode('raw_unicode_escape')
            string+='\n'
            send_num+=1
        num = start+send_num
        cursor.execute('update timeline set num=%s where wechat=%s',(num,wechat))
        cursor.close()
        conn.close()
        return string
    else:
        return hanzi.rdall
        cursor.close()
        conn.close()
    
if __name__ == '__main__':
    get_string('o1MyYt0yCh7P_Q4b36pfPxfmtLbk')

