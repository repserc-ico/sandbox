import mysql.connector as mydb
import sys

conn = mydb.connect(
 host='localhost',
 port='xxxx',
 user='root',
 password='passowrd',
 database='data'
)

print(conn.is_connected())
