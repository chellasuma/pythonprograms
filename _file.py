#file=open('sample.txt','w')
#data='''
#1.suma
##2.rani
#.lalli
#4.hari'''
#file.write(data)
#file.close()
import re
with open(r'C:\Users\\Administrator.MCA\\Desktop\\sumatext.txt','r+',encoding='utf-8') as file:
    data=file.read()
#print(data)
    a=re.sub('[ ]','_',data)
    file.seek(0)
    file.write(a)
