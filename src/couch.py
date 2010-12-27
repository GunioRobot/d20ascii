import couchdb
import json
import string
import yaml
import subprocess
import os

proc = subprocess.Popen('cat src/*/base-classes/*.yaml', shell=True, stdout=subprocess.PIPE, )
classfilesout = proc.communicate()[0]

couch = couchdb.Server()
try:
    del couch['d20']
except:
    pass
db=couch.create('d20')
print db

classes=yaml.load(classfilesout)
for taco in classes:
    name=taco['Name']
    taco['Type']="Class"
    db[name]=taco
