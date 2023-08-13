import mysql.connector # This module connects python with MySQL
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",# 127.0.0.1@3306 is local system so 'localhost' is written
  user="abc", # user name
  password="password" # Password
  # If we join some new company then admin will give us 'host', 'user' and 'password'. 
)
print(mydb)# prints the connection
mycursor = mydb.cursor()# This cursor/pointer variable enables us to execute any SQL command.
#mycursor.execute("SELECT *FROM test1.test_table")# It will show entire table
mycursor.execute("SELECT c1 ,c5 FROM test1.test_table") # If we want to see only two columns.
for data in mycursor.fetchall(): # fetchall() brings rows consecutively and returns in form of tuple.
    print(data