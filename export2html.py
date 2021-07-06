from tree import ScanDir
import re, os, sys

#generate index.html for github.io
toHtml = ScanDir()     
toHtml.export = True
toHtml.exportDir = "/home/mihai/export" 
toHtml.root = "/book"                   
toHtml.go()

headerDjangoTemplate = """
{% extends 'base.html' %}

{% load static %}

{% block content %}

    <div class="container">
      <div class="row">

      <!--<p style=""><a href="/book/about.html" target="_blank">About</a></p>-->

"""

footerDjangoTemplate = """

      </div>
    </div>

{% endblock content %}
"""

newString = headerDjangoTemplate + toHtml.string + footerDjangoTemplate

f = open(toHtml.exportDir + "/" + "ai.html", mode = 'w')
f.write(newString)
f.close()

#copy about.html
#cmd = "cp " + "about.html" + " " + toHtml.exportDir
#os.system(cmd)
#cmd = "cp " + "me2.png" + " " + toHtml.exportDir
#os.system(cmd)
#cmd = "cp " + "jeremy-thomas-E0AHdsENmDg-unsplash.jpg" + " " + toHtml.exportDir
#os.system(cmd)
