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
mycursor.execute("SHOW DATABASES")# SQL commands should be inside execute().
for x in mycursor:
  print(x)