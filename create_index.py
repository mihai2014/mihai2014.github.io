from tree import ScanDir
import re, os
import sys

#generate index.html for github.io
index = ScanDir()     
index.root = "https://nbviewer.jupyter.org/github/mihai2014/mihai2014.github.io/blob/master"
index.go()

# opens the file in reading mode
f1 = open("index.html", mode='r')
old_file_str = f1.read()
f1.close()

#replace content between <!--start topics--> and <!--end topics--> with topics string

begin = old_file_str.find("<!--start topics-->")
end = old_file_str.find("<!--end topics-->")

if(begin==-1 or end==-1):
    print("error")
    sys.exit()

end = end+len("<!--end topics-->")
#to replace part
#print(old_file_str[begin:end])

partOne = old_file_str[:begin]
partTwo = index.string         #replace part
partThree = old_file_str[end:]

new_file_str = partOne + "<!--start topics-->\n" + partTwo + "<!--end topics-->\n" + partThree

# opens the file in writing mode 
f2 = open("index2.html", mode = 'w')
f2.write(new_file_str)
f2.close()

#rewrite index1.html
os.system("cp index2.html index.html")
