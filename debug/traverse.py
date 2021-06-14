import os
import re
from names import names

startStr = "https://nbviewer.jupyter.org/github/mihai2014/mihai2014.github.io/blob/master"
startStr = ""
string = ""

def traverse_dir(dirName):

    global string
    string += '<ul>\n'

    for item in sorted(os.listdir(dirName)):

        fullpath = os.path.join(dirName, item)
        
        #==folder==
        if os.path.isdir(fullpath):
            string += ('<li>%s</li>\n' % item)

        #==file==    
        else:
            relativePath = startStr + fullpath
            string += ('<li><a href="%s">%s</a></li>\n' % (relativePath,item))

        if os.path.isdir(fullpath):
            if os.listdir(fullpath) != []:
                traverse_dir(fullpath)

    string += '</ul>\n'

traverse_dir('.')
#print(string)