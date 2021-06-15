from tree import ScanDir
import re, os

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



