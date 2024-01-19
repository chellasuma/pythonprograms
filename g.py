p1=eval(input('enter rock or paper or scissors'))
p2=eval(input('enter rock or paper or scissors'))
if p1==p2:
    print("match tie")

elif p1=='rock' and p2=='scissors':
     print('p1 win')
elif p1=='scissors'  and p2=='paper':
    print('p1 win')
elif p1=='paper' and p2=='rock':
    print('p1 win')
    
else:
    print("p2 win")
