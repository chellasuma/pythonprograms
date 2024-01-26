import csv
with open('new.csv','r' ,newline='') as file:
    
    records=csv.DictReader(file)
    for i in records:
        print(i)


         
    

    
    