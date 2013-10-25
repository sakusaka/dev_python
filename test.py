#!/usr/bin/python
# coding: utf-8

import os

#ファイルの存在を確認
flug = os.path.exists("./test.txt")
print flug

if flug:
    print "ファイルは存在します"
else:
    print "ファイルは存在しません"

