#!/usr/bin/python
# coding: utf-8

import MySQLdb

# DBへログイン
# localhostの場合は省略可
connection = MySQLdb.connect(db="test",user="test",passwd="test",port=3307, unix_socket='/usr/local/mysql/5.6.12/tmp/mysql-master.sock')

cursor = connection.cursor()
# SQL
cursor.execute("select * from test_table")
result = cursor.fetchall()

for i in range(2):
    for row in result:
         print row[0]
         cursor.close()

