import os, sys, codecs, json
import jieba
import jieba.analyse


# Defaults
config = {
    'root': '~/nomadic',
    'port': 9137,
    'default_notebook': '',
    'override_stylesheet': ''
}





def main():
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

    seg_list = jieba.cut(text, cut_all=False)
    fh = codecs.open('./seg/test.txt', 'w', 'utf-8')
    fh.write(' '.join(seg_list))

    tags = jieba.analyse.extract_tags(text, topK=10)
    print(",".join(tags))

    print 'done'




if __name__ == '__main__':
    main()
