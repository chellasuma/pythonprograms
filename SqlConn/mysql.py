import pymysql
import csv
conn=pymysql.Connection(user='root',password='root',host='localhost',port=3306,db='pythonsql')
cur=conn.cursor()


def createtable():
    query='''create table sumamca(
    id int auto_increment primary key,
    name varchar(50),
    age int,
    gender varchar(20),
    address varchar(20)
    );'''
    cur.execute(query)
def insertrecord(sid, name, age, gender, address):
    record=[sid, name, age, gender, address]
    
    cur.execute("insert into sumamca(id, name, age, gender, address) values(%s, %s, %s,%s,%s)",record)
    conn.commit()

def read_records():
    query='select * from sumamca'
    cur.execute(query)
    records=cur.fetchall()
    for row in records:
        print(row)
''' with open("records.csv",'w',newline='')  as csvfile:
        data=csv.writer(csvfile)
        data.writerow(['id','name','age','gender','address'])
        for row in records:
            data.writerow(row)
read_records()'''


#read_records()
def fetch_record(sid):
   query='select * from sumamca where id=%s'
   cur.execute(query,sid)
   records=cur.fetchall()
   for row in records:
       print(row)
#fetch_record(2)
def updatename(sid):
    fetch_record(sid)
    name=input('enter new name')
    record=[name,sid]
    query="update sumamca set name=%s where id=%s"
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)    
#updatename(2)
def updateage(sid):
    fetch_record(sid)
    age=int(input('enter new age'))
    record=[age,sid]
    query="update sumamca set age=%s where id=%s"
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)
#updateage(2)
def updateaddress(sid):
    fetch_record(sid)
    address=input('enter new address')
    record=[address,sid]
    query="update sumamca set address=%s where id=%s"
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)
#updateaddress(2)
def delete_record(sid):    
    query="delete from sumamca where id=%s"
    cur.execute(query,sid)
    conn.commit()    
#delete_record(2)
def truncate():
    query="truncate sumamca"
    cur.execute(query)
    conn.commit()
#truncate()
def read_rows():
    with open('records.csv','r',newline='')as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for row in range(1,len(data)):
            insertrecord(*data[row])

        
            
    
