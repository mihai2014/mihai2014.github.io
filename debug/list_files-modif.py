#generate index.html / topics

import sys
import os
import re
from names import names

DIR = "/home/mihai/export/"
HOST_DIR = "/book/"
EXPORT = True

string = ""

if(EXPORT):
    os.system("rm -rf /home/mihai/export/")

def export2html(dir_name, file_path):

    print(">>>",file_path)

    # copy png images
    match_png = re.search(r".png",file_path)
    if (match_png):
        cmd = "mkdir " + DIR + dir_name + "/"
        #maybe there is already
        try:
            print(cmd)
            #os.system(cmd)
        except:
            pass
        cmd = "cp " + file_path + " " + DIR + dir_name + "/"
        print(cmd)
        #os.system(cmd)

    # copy html files
    match = re.search(r".html",file_path)
    if match:
        match2 = re.search("/",file_path)
        #print(match2,file_path)
        #do not copy root files
        if(match2):
            cmd = "mkdir " + DIR + dir_name + "/"
            #maybe there is already
            try:
                print(cmd)
                #os.system(cmd)
            except:
                pass
            cmd = "cp " + file_path + " " + DIR + dir_name + "/"
            print(cmd)
            #os.system(cmd)
        else:
            cmd = ""
    # notebook file convert    
    else:
        #ex:   jupyter nbconvert ml/net1.ipynb --output-dir='/home/mihai/export/ml/'  --to html 
        cmd = "jupyter nbconvert " + file_path + " --output-dir='" + DIR + dir_name +  "' --to html "
        #print(cmd)
        #os.system(cmd)

    #??here, new dir structure are initiated by nbconvert
    #copy png files it there are any


def traverse_dir(dir_name):

    global string
    string += '<ul>\n'

    for item in sorted(os.listdir(dir_name)):
    #for item in filterList(os.listdir(dir_name)):

        #exclude folders: '.*', 'front-end', '__pycache__'
        avoid_dir = re.findall("^\.(.*)|(front-end)|(__pycache__)$",item)
        if( avoid_dir == []):

            fullpath = os.path.join(dir_name, item)

            if os.path.isdir(fullpath):
                string += ('<li>%s</li>\n' % item)
            else:

                #only *.html and *.ipynb
                html = re.findall("^(.*).html$",item)
                ipynb = re.findall("^(.*).ipynb$",item)

                avoid_file = re.findall("^(about_me.html)|(index.html)|(index2.html)|(content.html)|(dj.html)$",item)

                #only html and ipynb files
                if((html != [] or ipynb != []) and avoid_file == []):
                    if EXPORT:
                        startStr = HOST_DIR
                        #remove startStr
                        fullpath = fullpath[2:]
                    else:    
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
                    if EXPORT:
                        export2html(dir_name[2:],fullpath)
                        relativePath = relativePath.replace(".ipynb",".html")
                        
                    string += ('<li><a href="%s" target="_blank" rel="noopener noreferrer">%s</a></li>\n' % (relativePath,item))


            if os.path.isdir(fullpath):
                if os.listdir(fullpath) != []:
                    traverse_dir(fullpath)

    string += '</ul>\n'

traverse_dir('.')
#print(string)
if(EXPORT):
    f = open(DIR + "ai.html", mode = 'w')
    f.write(string)
    f.close()
    sys.exit()    

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
