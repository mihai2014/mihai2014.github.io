import os
import re
from names import names

class ScanDir:

    def __init__(self):
        self.export = False
        self.exportDir = "/home/mihai/export"
        self.string = ""
        self.root = ""  #root index for topics links
        self.rootDir = "."
        self.reFilterDir = "^\.(.*)|(front-end)|(__pycache__)|(debug)$"
        self.reFilterFiles = ""

    def initExportDir(self):
        
        os.system("rm -rf /home/mihai/export/")
        os.system("mkdir /home/mihai/export/")


    def toHtml(self, fullpath, dirName, item):
        # export notebooks to html
        # erase '.' from the beggining of fullpath below...
        
        #===folder===
        if os.path.isdir(fullpath):

            self.string += ('<li>%s</li>\n' % item)
            cmd = "mkdir " + self.exportDir + fullpath[1:] + "/"
            os.system(cmd)

        #===file===
        else:
            #filter root files       
            if(dirName != "."):
                
                relativepath = self.root + fullpath[1:]
                #rename item if defined alternate name
                try:
                    renamedItem = names[item]
                except:
                     renamedItem = item
                        
                if(re.search(r".html",item)):
                    #copy html and png file    
                    cmd = "cp " + fullpath[2:] + " " + self.exportDir + fullpath[1:] 
                    os.system(cmd)

                    #create html topic link
                    self.string += (f"<li><a href=\"{relativepath}\" target=\"_blank\" rel=\"noopener noreferrer\">{renamedItem}</a></li>\n")

                if(re.search(r".png",item)):
                    #copy html and png file    
                    cmd = "cp " + fullpath[2:] + " " + self.exportDir + fullpath[1:] 
                    os.system(cmd)

                    #no need for link

                if(re.search(r".ipynb",item)): 
                    #convert notebook
                    #ex:   jupyter nbconvert ml/net1.ipynb --output-dir='/home/mihai/export/ml/'  --to html 
                    cmd = "jupyter nbconvert " + fullpath[2:] + " --output-dir='" + self.exportDir + dirName[1:] +  "' --to html --template mihai"
                    os.system(cmd)  

                    #create html topic link
                    newlink = relativepath.replace(".ipynb",".html")    
                    #self.string += (f"<li><a href=\"{newlink}\" target=\"_blank\" rel=\"noopener noreferrer\">{renamedItem}</a></li>\n")    
                    self.string += (f"<li><a href=\"{newlink}\" >{renamedItem}</a></li>\n")

    def createTopics(self, fullpath, dirName ,item):
        
        #generate tree html links of files
        # erase '.' from the beggining of fullpath below
        # ---------------------------------------------------------------
        
        #===folder===
        if os.path.isdir(fullpath):
            self.string += ('<li>%s</li>\n' % item)

        #===file===    
        else:
            #filter only notebooks and html ?
            matchFiles = re.search(".html|.ipynb",item)
            #filter root files       
            if(dirName != "." and matchFiles):
                relativepath = self.root + fullpath[1:]
                #rename item if defined alternate name
                try:
                    item = names[item]
                except:
                    pass                
                self.string += (f"<li><a href=\"{relativepath}\" target=\"_blank\" rel=\"noopener noreferrer\">{item}</a></li>\n")
            
        # ---------------------------------------------------------------


    def scan_tree(self,dirName):    
        
        self.string += '<ul>\n'

        for item in sorted(os.listdir(dirName)):
            
            filterDir = re.search(self.reFilterDir,item)

            #filter folders
            if(not filterDir):

                fullpath = os.path.join(dirName, item)
                
                if(self.export):
                    self.toHtml(fullpath, dirName, item) 
                else:
                    self.createTopics(fullpath, dirName, item)    

                if os.path.isdir(fullpath):
                    if os.listdir(fullpath) != []:
                        self.scan_tree(fullpath)

        self.string += '</ul>\n'


    def go(self):
        if(self.export): self.initExportDir()
        self.scan_tree(self.rootDir)
        
        
