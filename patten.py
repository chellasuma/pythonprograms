#rows=int(input('enter number of rows:-'))
'''for i in range(1,rows+1):
    for j in range(1,rows+1):
        print('*',end='')
 
         print()'''
rows=int(input('enter number of rows:'))
out=''

for i in range(rows):
    for j in range(rows):              
         if i==j or i==rows-j-1:        
            out+=' '
         else:
            out+='* '
    out+='\n'
n=input('enter file name:')
with open(f'{n}.txt','w')as file:
    file.write(out)
    
    