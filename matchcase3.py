n=int(input('enter number:'))
match n%2:
        case 0:
        # if n%2==0:
             print(n**2)
        case 1:            
            print(n**3)
        case _:
            print('invalid input')
    
