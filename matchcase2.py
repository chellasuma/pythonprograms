a=int(input('enter value for a:'))
b=int(input('enter value for b:'))
c=input('enter airthematic operator for c:-')

match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case '//':
        print(a//b)
    case '**':
        print(a**b)
    
    case _:
        print('invalid input')