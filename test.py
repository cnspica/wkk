import os, shutil

# process input
encoding = "utf-8"
dirname = ''
if not os.path.isdir('Notes/evernote'):
    os.mkdir('Notes/evernote')
dirs = os.listdir('Import')
for d in dirs:
    if os.path.isdir('Import/'+d):
        dirname = d
        dirname = dirname.decode(encoding)
        files = os.listdir('Import/'+dirname)
        for f in files:
            if f[0] == '.': continue
            if os.path.isdir('Import/'+dirname+'/'+f): continue
            print f
            filename = f
            filename = filename.decode(encoding)
            data = open('Import/'+dirname+'/'+filename, 'rb').read()
            data = data.decode(encoding)
            filename_arr = filename.split('.')

            if os.path.exists('Import/'+dirname+'/'+filename+".resources"):
                if not os.path.isdir('Notes/evernote/'+dirname+'/_resources'):
                    os.mkdir('Notes/evernote/'+dirname+'/_resources')
                replacestr = filename_arr[0]+'.resources'
                data.replace(replacestr, '_resources')
                pics = os.listdir('Import/'+dirname+'/'+replacestr)
                for p in pics:
                    shutil.copyfile('Import/'+dirname+'/'+replacestr + "/" + p,'Notes/evernote/'+dirname+'/_resources' + filename_arr[0] + p)
                print data
'''
            h = HTML2Text(baseurl=baseurl)
            # handle options
            if options.ul_style_dash: h.ul_item_mark = '-'
            if options.em_style_asterisk:
                h.emphasis_mark = '*'
                h.strong_mark = '__'

            h.body_width = options.body_width
            h.list_indent = options.list_indent
            h.ignore_emphasis = options.ignore_emphasis
            h.ignore_links = options.ignore_links
            h.ignore_images = options.ignore_images
            h.google_doc = options.google_doc
            h.hide_strikethrough = options.hide_strikethrough
            h.escape_snob = options.escape_snob

            # wrapwrite(h.handle(data))
            f =codecs.open('Notes/evernote/'+dirname+'/'+filename_arr[0]+'.md',"w","utf-8")
            f.write(h.handle(data))
            '''
