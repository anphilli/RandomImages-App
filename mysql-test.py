#!/usr/bin/env python

import pymysql.cursors
import pymysql
import os

# Connect to the database
conn = connection = pymysql.connect(host='10.8.29.11',
                             user='root',
                             password='cisco123',
                             db='images',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


cur = conn.cursor()

with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT *  FROM imagestable"
    cursor.execute(sql)
    result = cursor.fetchone()
    imagelocation = (result.get('imagefile'))

print (imagelocation)
    # os.system('open {}'.format(imagelocation))
