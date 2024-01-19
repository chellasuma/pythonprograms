a='user@123#admin'
b=' '
for i in a:
    if not i in '0123456789':
        b+=i
    
print(b)



