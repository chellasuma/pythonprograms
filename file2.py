'''file=open(r"C:\\Users\Administrator.MCA\\Desktop\damu\\datatable.py",'r')
data=file.read()
#print(data)
file.close()
import re
a=re.findall('[aeiouAEIOU]',data)
print(a)
print(len(a))'''
import re
#a=re.findall('[a-zA-Z0-9]+\.?[a-zA-Z0-9]*\@gmail\.com','abcd123xyz.123@gmail.com')
#print(a)
a=re.sub('[aeiou]','*','happy republic day')
print(a)