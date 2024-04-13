from mysql import connector

#python -m pip install mysql-connector-python
#pip3 install mysql-connector-python

def createTable():
     table = 'create table employee(id int primary key auto_increment,\
     name varchar(50),\
     phone varchar(20))'
     return table

def insertEmployee():
     empSql = 'insert into employee(name, phone) values(%s,%s)'
     return empSql
try:
    conn = connector.connect(
        host='localhost',
        port=8889,
        user='root',
        password='root',
        database='synechron'
    )
    if conn.is_connected():
            print('Connected to MySQL database')
    cursor = conn.cursor()
    #cursor.execute(createTable())
    cursor.execute(insertEmployee(),('riya','1212121212')) 
    conn.commit()
    #cursor.execute('create database synechron')
except Exception as e:
    print(e)
finally:
    conn.close()
