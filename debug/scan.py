import os
import re
from names import names

root = "https://nbviewer.jupyter.org/github/mihai2014/mihai2014.github.io/blob/master"
root = ""
string = ""

def traverse_dir(dirName):

    global string
    string += '<ul>\n'

    for item in sorted(os.listdir(dirName)):

        avoid_dir = re.findall("^\.(.*)|(front-end)|(__pycache__)$",item)
        #avoid_file = re.findall("^(about_me.html)|(index.html)|(index2.html)|(content.html)|(dj.html)$",item)

        #avoid folders
        if(not avoid_dir):

            fullpath = os.path.join(dirName, item)
            
            # ---------------------------------------------------------------
            
            #===folder===
            if os.path.isdir(fullpath):
                string += ('<li>%s</li>\n' % item)

            #===file===    
            else:
                #avoid root files       
                if(dirName != "."):
                    # erase '.' from the beggining of fullpath
                    relativepath = root + fullpath[1:]
                    string += ('<li><a href="%s">%s</a></li>\n' % (relativepath,item))
                
            # ---------------------------------------------------------------

            if os.path.isdir(fullpath):
                if os.listdir(fullpath) != []:
                    traverse_dir(fullpath)

    string += '</ul>\n'

traverse_dir('.')
print(string)