#!/usr/bin/env python
#-*- coding=utf-8 -*-

from os.path import join, dirname, abspath, exists
import time

from lxml import etree
import logbook

import api

def directmsg():
    xml = api.get('direct_messages/inbox')
    if xml:
        xml = etree.fromstring(xml)
        num = len(xml)
        if num > 0:
            for i in range(num):
                id = xml[i][0].text
                msg = xml[i][1].text
                logbook.info(msg.encode("utf8"))
                sendtext(msg.encode("utf8"))
                code = api.post('direct_messages/destroy', id=id)
                logbook.info("destory")
                while code != 1:
                    code, xml = api.fanfou('direct_messages/destroy',{'id':id})

def sendtext(content):
    xml = api.get('account/rate_limit_status')
    xml = etree.fromstring(xml)
    limit_num = xml[1].text
    if int(limit_num) == 0:
        return
    code = api.post('statuses/update',status=content)
    logbook.info("sent!")

if __name__ == '__main__':
    server_log_file = join(dirname(abspath(__file__)), "log/wechat.log")
    if not exists(server_log_file):
        open(server_log_file, "w").close()

    local_log = logbook.FileHandler(server_log_file)
    local_log.format_string = (
        u'[{record.time:%H:%M:%S}] '
        u'lineno:{record.lineno} '
        u'{record.level_name}:{record.message}')
    local_log.push_application()

    while True:
        directmsg()
        time.sleep(60)
