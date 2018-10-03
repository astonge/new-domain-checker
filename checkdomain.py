#!/usr/bin/env python3

import socket
import sys

def getip(d):
  try:
    data = socket.gethostbyname(d)
    ip = repr(data)
    return ip[1:-1]
  except Exception:
    return "NULL"

for line in sys.stdin:
  domain = line.strip()
  print("%s:%s" % (domain,getip(domain)))
