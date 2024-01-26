n=int(input('enter number from 0-6 :-'))

match n:
    case 0:
        print('sunday')
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thrsday')
    case 5:
        print('friday')
    case 6:
        print('satruday')
    
    case _:
        print('invalid input')
