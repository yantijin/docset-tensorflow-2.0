# -*- coding: utf-8 

import markdown
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def md2html(mdstr, k):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    # html1 = '''
    # <html lang="zh-cn">
    # <head>
    # <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    # <link href="
    # ''' + '../'*k
    # html2 ='''
    # default.css" rel="stylesheet">
    # <link href="
    # ''' + '../'*k
    # html3 = '''
    # github.css" rel="stylesheet">
    # </head>
    # <body>
    # %s
    # </body>
    # </html>
    # '''
    # print(html1+html2+html3)
    html1 = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="''' 
    html2 ='''default.css" rel="stylesheet">
    <link href="
    ''' 
    html3 = '''github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''
    html = html1+'../'*k+html2[:-1]+'../'*k+html3[:-1]
    print(html)

    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret

def getName():
    root ='./out'
    mat_name = [os.path.join(path, file_name) 
                for path, _, file_list in os.walk(root) 
                for file_name in file_list if file_name.endswith('.md')]
    return mat_name

if __name__ == '__main__':

    # if len(sys.argv) < 3:
    #     print('usage: md2html source_filename target_file')
    #     sys.exit()
    names = getName()
    print(names)
    for name in names:
        name2 = name[:-2] + 'html'
        k=-1
        for i in range(len(name)):
            if name[i] == '/':
                k+=1
        infile = open(name, 'r')
        md = infile.read()
        infile.close()
        if os.path.exists(name2):
            os.remove(name2)


        outfile = open(name2,'a')
        outfile.write(md2html(md, k))
        outfile.close()



    # infile = open(sys.argv[1],'r')
    # md = infile.read()
    # infile.close()


    
    # if os.path.exists(sys.argv[2]):
    #     os.remove(sys.argv[2])


    # outfile = open(sys.argv[2],'a')
    # outfile.write(md2html(md))
    # outfile.close()

    # print('convert %s to %s success!'%(sys.argv[1],sys.argv[2]))
