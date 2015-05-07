# -*- coding: utf-8 -*-

import os, sys, codecs, json, re
import jieba
import jieba.analyse
import stopwordsfilter

noteroot = '../Notes'
testnote = '../Notes/china-and-world.md'
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

def findsimilarity(note):
    h = codecs.open(note, 'r')
    text = h.read()
    tags = jieba.analyse.extract_tags(text, topK=30)
    loadtagbase()
    ismatch = 0

    tags = stopwordsfilter.stopwordsfilter(tags)

    # start matching
    for tagline in tagbase:
        #tagline is a set of tags for notes
        ismatch = 0
        matchtags = ''
        for tag in tags:
            # tag is one of the tags for testnote
            for mtag in tagline:
                # mtag is one of the tags in one file of the tagbase
                if tag == mtag:
                    # if there is a tag same as the testnote's tag, we add it to the list
                    ismatch = 1
                    matchtags = matchtags + tag + " "
        if ismatch == 1:
            matchnotes.append(tagline[0] + " " + matchtags)

    print '[Original Notes]'
    print note
    print 'Similar Notes:'
    for nt in matchnotes:
        print nt

if __name__ == '__main__':
    findsimilarity(testnote)
