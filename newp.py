for i in range(2,201):
     for j in range(2,201):
         if i%j==0:
            break
         if i==j:
             print(i,end=', ')
            