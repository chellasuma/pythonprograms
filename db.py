db={'username':'chellasuma','password':"sumaMCA@123"}
username=eval(input("Enter username"))
password=eval(input("Enter password"))

if  db['username']==username and db['password']==password:
    print('succefull')
else:
    print('invalid username or password')