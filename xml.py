#!/usr/bin/env python
#-*- coding=utf-8 -*-

import message
from lxml     import etree
import chardet
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class xmlmsg:
    def GET(self):
        for i in range (703,0,-1):
            f   = file('/var/www/fanfou/treeholes/'+str(i)+'.xml')
            xml = f.read()
            f.close()
            xml = etree.fromstring(xml)
            for j in range(len(xml)-1,-1,-1):
                talk = xml[j][0].text.encode('utf-8')
                message.save(talk,0)
            
