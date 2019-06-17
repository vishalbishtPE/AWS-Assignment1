import pymysql

def connection():
    try:
        conn = pymysql.connect(host="host_name",user="usename",passwd="Borkar11",port=3306, db="Game" )
        print("connected.")
        return conn
    except Exception as e:
        print(e)

# prepare a cursor object using cursor() method
db = connection()
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)
print("created table")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('sela', 'Harman', 70, 'M', 7900)")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('sam', 'KUnal', 45, 'M', 5000)")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Harini', 30, 'F', 8700)")



cursor.execute("Select * from  EMPLOYEE")
results = cursor.fetchall()
print(results)

#delete

cursor.execute("DELETE FROM EMPLOYEE WHERE AGE < 35 ")

#update

cursor.execute("UPDATE EMPLOYEE SET AGE = AGE + 5 WHERE SEX = 'F'")

print(cursor.execute("Select * from EMPLOYEE"))
results = cursor.fetchall()
print(results)

#select to see the update

cursor.execute("Select * from  EMPLOYEE")


