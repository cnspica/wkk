import os, sys, codecs, json
import jieba
import jieba.analyse
from snownlp import SnowNLP


# Defaults
config = {
    'root': '~/nomadic',
    'port': 9137,
    'default_notebook': '',
    'override_stylesheet': ''
}





def wordseg(method):
    cfg_path = os.path.expanduser(u'~/.nomadic')
    # Open the config file.
    with open(cfg_path, 'r') as cfg_file:
        user_cfg = json.load(cfg_file)
        config.update(user_cfg)

    notepath = config['root']

    #testnote = str(notepath + '/wdxtub.md')

    testnote = '../Notes/wdxtub.md'
    h = codecs.open(testnote, 'r', 'utf-8')
    text = h.read()


    if method == 1:
        seg_list = jieba.cut(text, cut_all=False)
        fh = codecs.open('./seg/test.txt', 'w', 'utf-8')
        fh.write(' '.join(seg_list))
        tags = jieba.analyse.extract_tags(text, topK=10)
        print(",".join(tags))
    elif method == 2:
        s = SnowNLP(text)

        for w in s.keywords(10):
            print w.encode('utf-8')

        for su in s.summary(3):
            print su.encode('utf-8')

    print 'done'




if __name__ == '__main__':
    wordseg(1)
