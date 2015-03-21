# -*- coding: utf-8 -*-

import os, sys, codecs, json, re
import jieba
import jieba.analyse

noteroot = '../Notes/hero'
testnote = '../Notes/wdxtub.md'
tburl = './seg/tags.txt'
tagbase = []
matchnotes = []
# this two sentence can solve Chinese Problem
reload(sys)
sys.setdefaultencoding('utf-8')


def loadtagbase():
    tagfile = codecs.open(tburl, 'r')
    for tagline in tagfile:
        tagbase.append(tagline[:-len('\n')].split(' '))

def findsimilarity():
    h = codecs.open(testnote, 'r')
    text = h.read()
    tags = jieba.analyse.extract_tags(text, topK=15)
    loadtagbase()
    '''
    for tag in tags:
        print tag + ' ',
    print ''

    for tag in tagbase[0]:
        print tag + ' ',
    print ''
    '''
    # start matching
    for tagline in tagbase:
        #tagline is a set of tags for notes
        for tag in tags:
            # tag is one of the tags for testnote
            for mtag in tagline:
                # mtag is one of the tags in one file of the tagbase
                if tag == mtag:
                    # if there is a tag same as the testnote's tag, we add it to the list
                    matchnotes.append(tagline[0])
                    continue

    print 'Original Notes'
    print '把你的笔记用起来'
    print 'Similar Notes:'
    for note in matchnotes:
        print note

if __name__ == '__main__':
    findsimilarity()
