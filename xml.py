#!/usr/bin/env python
#-*- coding=utf-8 -*-

from database import message
from lxml     import etree
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class xmlmsg:
    def GET(self):
        for i in range (703,-1,-1):
            f   = file('/var/www/fanfou/treeholes/'+str(i)+'.xml')
            xml = f.read()
            xml = etree.fromstring(xml)
            for j in range(len(xml)-1,-1,-1):
                message.save(xml[j][0].text+'  '+xml[j][1].text,0)
