import re

#match = re.findall("<!--a-->.*<!--b-->","iii<!--a--> 123    <!--b-->iii")
#print(match)
#new = re.sub("<!--a-->.*<!--b-->" , "ceva"   ,"iii<!--a--> 123    <!--b-->iii")
#print(new)

#s= "start<!--start topics-->between<!--end topics-->end"
#match = re.findall("<!--start topics-->.*<!--end topics-->",s)
#print(match)
#new = re.sub("<!--start topics-->.*<!--end topics-->","ceva",s)
#print(new)

#re.sub(r'a', 'b', 'banana')
#'bbnbnb'

#re.sub(r'/\d+', '/{id}', '/andre/23/abobora/43435')
#'/andre/{id}/abobora/{id}'

match = re.search(".html|.ipynb","asdfasdfadf.ipynb")
print(match)
