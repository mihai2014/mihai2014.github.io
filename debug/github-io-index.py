#generate index.html for github io site

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

# opens the file in reading mode
f1 = open("index.html", mode='r')
old_file_str = f1.read()
f1.close()

#replace content between <!--start topics--> and <!--end topics--> with string
#print(file_str)
new_file_str = re.sub("^(<!--start topics-->.*<!--end topics-->)$","<!--start topics-->\n" + string  + "\n<!--end topics-->",old_file_str)

# opens the file in writing mode 
f2 = open("index2.html", mode = 'w')
f2.write(new_file_str)
f2.close()

os.system("cp index2.html index.html")
