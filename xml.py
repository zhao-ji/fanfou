#!/usr/bin/env python
#-*- coding=utf-8 -*-

from database import message
from lxml     import etree
import chardet
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class xmlmsg:
    def GET(self):
        for i in range (703,0,-1):
            f   = file('/home/nightwish/Music/fanfou/treeholes/'+str(i)+'.xml')
            xml = f.read()
            f.close()
            try:
                xml = etree.fromstring(xml)
            except Exception,e:
                m   = file('/home/nightwish/Music/fanfou/error.txt','a')
                s = '文件：%d.xml  :%s' %(i,e)
                m.write(s)
                m.close()
            for j in range(len(xml)-1,-1,-1):
                try:
                    talk = xml[j][0].text.encode('utf-8')
                except Exception,e:
                    m   = file('/home/nightwish/Music/fanfou/error.txt','a')
                    s = '文件：%d.xml  第%d行   :%s' %(i,j,e)
                    m.write(s)
                    m.close()
                message.save(talk,0)
