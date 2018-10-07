#!/usr/bin/env python3

import socket
import sys
import sqlite3
import os.path

def getip(d):
  try:
    data = socket.gethostbyname(d)
    ip = repr(data)
    return ip[1:-1]
  except Exception:
    return "NULL"

DB = "new_domains.db"
if os.path.exists(DB):
  db = sqlite3.connect(DB)
  print("Connected to database..")
  # for line in sys.stdin:
  # domain = line.strip()
  # print("%s:%s" % (domain,getip(domain)))
  cursor = db.cursor()
  cursor.execute('''SELECT domain FROM domains LIMIT 10''')
  domain_list = cursor.fetchall()
  for d in domain_list:
      print("%s:%s" % (d[0],getip(d[0])))
  db.close()
else:
  print("DATABASE NOT FOUND")
  print("RUN ./importdomains FIRST")
  exit(-1)
