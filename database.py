 # importing the module
import MySQLdb
#import mysql.connector
#conn = mysql.connector.connect(host='localhost',database='attendance',user='root',password='root')# opening a database connection
db = MySQLdb.connect  ("localhost","root","root","attendance")

# define a cursor object
cursor = db.cursor()
name = input("name:")
# drop table if exists
#cursor.execute("IF STUDENT TABLE EXISTS DROP IT")
sql1 = "UPDATE `attendance`.`students` SET `attendence`='absent	' WHERE `name`='%s'"%(name)
# query
sql = " SELECT * FROM attendance.students;"
# execute query
cursor.execute(sql1)
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
# close object
db.commit()
cursor.close()

# close connection
db.close()
print("Sent Successfully")
