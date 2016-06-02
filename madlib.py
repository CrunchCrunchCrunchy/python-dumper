import os,re
openfile=open('C:\\rpf\\python\\madlibtxt.txt')
mlre=re.compile(r'[A-Z][A-Z]+')
mlcontent=openfile.read()
print(mlcontent)
mo=mlre.findall(mlcontent)
print(mo)

