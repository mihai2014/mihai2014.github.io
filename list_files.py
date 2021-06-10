#generate index.html / topics

import os
import re
from names import names

string = ""

def traverse_dir(dir):

    global string
    string += '<ul>\n'

    for item in sorted(os.listdir(dir)):
    #for item in filterList(os.listdir(dir)):

        #exclude folders: '.*', 'front-end', '__pycache__'
        avoid_dir = re.findall("^\.(.*)|(front-end)|(__pycache__)$",item)
        if( avoid_dir == []):

            fullpath = os.path.join(dir, item)

            if os.path.isdir(fullpath):
                string += ('<li>%s</li>\n' % item)
            else:

                #only *.html and *.ipynb
                html = re.findall("^(.*).html$",item)
                ipynb = re.findall("^(.*).ipynb$",item)

                avoid_file = re.findall("^(about_me.html)|(index.html)|(content.html)|(dj.html)$",item)

                #only html and ipynb files
                if((html != [] or ipynb != []) and avoid_file == []):
                    #startStr = PWD + "/blog/templates/blog/data"
                    startStr = "https://nbviewer.jupyter.org/github/mihai2014/mihai2014.github.io/blob/master"
                    #remove startStr
                    fullpath = fullpath[1:len(fullpath)]

                    #rename
                    try:
                        item = names[item]
                    except:
                        pass

                    relativePath = startStr + fullpath
                    string += ('<li><a href="%s">%s</a></li>\n' % (relativePath,item))


            if os.path.isdir(fullpath):
                if os.listdir(fullpath) != []:
                    traverse_dir(fullpath)

    string += '</ul>\n'

traverse_dir('.')
print(string)

#ttps://nbviewer.jupyter.org/github/mihai2014/python-data-processing/blob/master
