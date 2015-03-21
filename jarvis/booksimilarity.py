# -*- coding: utf-8 -*-

import os, sys, codecs, json, re
import jieba
import jieba.analyse

testnote = '../Notes/wdxtub.md'
bburl = './seg/books.txt'
bookbase = []
matchbooks = []
# this two sentence can solve Chinese Problem
reload(sys)
sys.setdefaultencoding('utf-8')


def loadbookbase():
    bookfile = codecs.open(bburl, 'r')
    for bookline in bookfile:
        bookbase.append(bookline[:-len('\n')].split(' '))

def findsimilarity():
    h = codecs.open(testnote, 'r')
    text = h.read()
    tags = jieba.analyse.extract_tags(text, topK=15)
    loadbookbase()
    '''
    for tag in tags:
        print tag + ' ',
    print ''

    for tag in tagbase[0]:
        print tag + ' ',
    print ''
    '''
    # start matching
    for bookline in bookbase:
        #tagline is a set of tags for notes
        for tag in tags:
            # tag is one of the tags for testnote
            for mtag in bookline:
                # mtag is one of the tags in one file of the tagbase
                if tag == mtag:
                    # if there is a tag same as the testnote's tag, we add it to the list
                    matchbooks.append(bookline[0])
                    continue

    print 'Original Notes'
    print '把你的笔记用起来'
    print 'Related Books:'
    for book in matchbooks:
        print book

if __name__ == '__main__':
    findsimilarity()
