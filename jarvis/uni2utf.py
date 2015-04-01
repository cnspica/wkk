# -*- coding: utf-8 -*-

import os, sys, codecs, json

usertag = codecs.open('data/doubanbooks/bookusertag.txt', 'r')

js = json.loads(usertag.read())

fh = codecs.open('data/test.txt', 'w', 'utf-8')

fh.write(json.dumps(js, ensure_ascii=False))

print 'done'
