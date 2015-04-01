import os, sys, codecs, json, re
import jieba
import jieba.analyse

usertagbase = './data/doubanbooks/bookusertag.txt'
# this two sentence can solve Chinese Problem
reload(sys)
sys.setdefaultencoding('utf-8')

def usertagproc():
    usertaginfos = open(usertagbase,'r')
    count = 0
    fh = codecs.open('data/usertag.txt', 'w', 'utf-8')
    output = ''
    for usertag in usertaginfos:
        target = json.JSONDecoder().decode(usertag)

        print 'output line ' + str(count + 1)
        output = output + str(target['count'])
        output = output + ' [' + target['id'] + ']'
        for tag in target['tags']:
            output = output + ' ' + tag['title'] + ' ' + str(tag['count'])
        output = output + '\n'

        if count < 10:
            print target['count']
            print target['id']
            for tag in target['tags']:
                print tag['title'] + ' ' + str(tag['count'])

        count = count + 1

    fh.write(output)
    print 'Total ' + str(count) + ' Users'

if __name__ == '__main__':
    usertagproc()
