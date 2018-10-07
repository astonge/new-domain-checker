#!/usr/bin/env python

import os.path
import os
import sys
import sqlite3
import docker

docker_client = docker.from_env()
ARGS = "-v -nodns -norecursion -noalts"
CMDSTR = ""
DB = "new_domains.db"
if os.path.exists(DB):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('''SELECT domain FROM domains''')
    domain_list = cursor.fetchall()
    for d in domain_list:
        cmd = "docker run -t amass-docker %s -d %s" % (ARGS, d[0])
        print(cmd)
    db.close()
else:
    print("error")