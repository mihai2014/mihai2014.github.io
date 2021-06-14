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

        avoid_dir = re.findall("^\.(.*)|(front-end)|(__pycache__)(debug)$",item)
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


# opens the file in reading mode
f1 = open("index.html", mode='r')
old_file_str = f1.read()
f1.close()

#replace content between <!--start topics--> and <!--end topics--> with string
#print(file_str)
new_file_str = re.sub("^(<!--start topics-->.*<!--end topics-->)$","<!--start topics-->\n" + string  + "\n<!--end topics-->",old_file_str)
#print(new_file_str)

# opens the file in writing mode 
f2 = open("index2.html", mode = 'w')
f2.write(new_file_str)
f2.close()

os.system("cp index2.html index.html")