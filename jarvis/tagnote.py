# -*- coding: utf-8 -*-

import os, sys, codecs, json, re
import jieba
import jieba.analyse

noteroot = '../Notes/hero'
# this two sentence can solve Chinese Problem
reload(sys)
sys.setdefaultencoding('utf-8')

def noteproc():
    files = os.listdir(noteroot)
    taglist = []
    for f in files:
        if f[0] == '.': continue
        if os.path.isdir(noteroot+ '/' + f): continue
        # load note
        h = codecs.open(noteroot+ '/' + f, 'r')
        text = h.read()
        # clean timestamp in notes -> need to be a function
        # TODO eliminate ![]() tag
        text = re.sub(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d','', text)
        text = re.sub(r'\d\d\d\d-\d\d-\d\d','', text)
        text = re.sub(r'![.*](.*)','',text)
        text = re.sub(r'[.*](.*)','',text)
        # get top 10 tags with weights
        tags = jieba.analyse.extract_tags(text, topK=15, withWeight=True)
        # store to a list
        output = '[' + f + ']'
        print f,
        for t in tags:
            print ' ' + t[0],
            output = output + u' ' + t[0]
        print ''
        taglist.append(output + '\n')

    fh = codecs.open('./seg/tags.txt', 'w', 'utf-8')
    for t in taglist:
        fh.write(t)

    print 'done'

if __name__ == '__main__':
    noteproc()
