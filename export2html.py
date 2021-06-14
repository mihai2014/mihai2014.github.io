from tree import ScanDir
import re, os

#generate index.html for github.io
toHtml = ScanDir()     
toHtml.export = True
toHtml.exportDir = "/home/mihai/export" 
toHtml.root = "/book"                   
toHtml.go()

f = open(toHtml.exportDir + "/" + "ai.html", mode = 'w')
f.write(toHtml.string)
f.close()



