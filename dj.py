import re

f = open("nn_defs.html", mode = 'r')
htmlFile = f.read()
#print(htmlFile)
blockTags = re.findall("<!-- blocktags -->(.*)<!-- endblocktags -->",htmlFile,	re.DOTALL)[0]
blockContent = re.findall("<!-- blockcontent -->(.*)<!-- endblockcontent -->",htmlFile,    re.DOTALL)[0]
f.close()

#print(blockTags)
#print(blockContent)

newFile = """
{% extends 'base2.html' %}
{% load static %}

""" + \
"{% block tags %}\n" + \
blockTags + \
"{% endblock tags %}\n\n"+ \
"{% block content %}\n" + \
blockContent + \
"{% endblock content %}"

#print(newFile)

#convert links to /static/notebooks/...

newFile2 = ""

for line in newFile.split("\n"):
    src = re.findall("src=\"(.*)\" ",line)
    if(src):
        src = src[0]
        newsrc = "/static/notebooks/" + src
        #print(newsrc)
        line = line.replace(src,newsrc)
    newFile2 += line + "\n"

print(newFile2)    
