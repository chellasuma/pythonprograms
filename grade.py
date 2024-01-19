g=float(input('enter percentage'))
if g>=90 and g<=100:
    print("A+")
elif g>=80 and g<=90:
    print('A')
elif g>=70 and g<=80:
    print('B+')
elif g>=60 and g<=70:
    print('B')
elif g>=50 and g<=60:
    print('C+')
elif g>=35 and g<=50:
    print('C')
elif  g<35:
    print('F')
else:
    print('invalid marks')
