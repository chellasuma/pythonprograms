r=int(input('enter r:-'))
for i in range(r):
    for j in range(r):
        if i==r//2 :
            print(' ',end='')
        elif j==r//2:
            print(' ',end='')
        else:
            print('* ',end='')
    print()