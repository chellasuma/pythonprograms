class MNOError(Exception):
    pass
class nameError(Exception):
    pass
try:
    name=input(' name mobilenumber:-')
    if len(name)<=4:
            raise nameError(f'name should be more than 4 character but {len(name)} were given ')
    else:
        print('name is accepted')
    mno=input(' enter mobilenumber:-')
    if len(mno)!=10:
            raise MNOError(f'mobile number should be 10 digits but {len(mno)} were given ')
    else:
        print('mobile number is accepted')
except(MNOError,nameError) as e:
     print(e)
     

