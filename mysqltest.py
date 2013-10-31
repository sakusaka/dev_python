#!/usr/bin/python
# coding: utf-8

import MySQLdb

# DBへログイン
# localhostの場合は省略可
connection = MySQLdb.connect(db="test",user="root",password="",port=3306)

cursor = connection.cursor()
# SQL
cursor.execute("select * from users")
result = cursor.fetchall()

for row in result:
     p row[0]

     cursor.close()
     connection.close()

