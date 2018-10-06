#!/usr/bin/env python

import sqlite3

db = sqlite3.connect('testdomain.db')
print("Connected to database..")

cursor = db.cursor()
cursor.execute('''SELECT domain FROM domains''')
domain_list = cursor.fetchall()
for d in domain_list:
    print(d)

print("Closeing database connection..")
db.close()
