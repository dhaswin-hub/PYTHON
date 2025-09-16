f1=open('file1.text','r')
f3=open('file3.text','w')
l=f1.readline()
while (l!=""):
    f3.write(l)
    l=f1.readline()
f1.close()
f3.close()
