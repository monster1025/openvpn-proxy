import os
import re

nameserver = os.getenv('NAMESERVER')
if nameserver == None:
	print("NAMESERVER not specified, skipping proxy configuration")
	os._exit(-1)

filename = "/3pr.cfg"

with open(filename, 'r') as file :
  filedata = file.read()

if 'nserver' in filedata:
 filedata = re.sub(r'nserver .*', 'nserver {}'.format(nameserver), filedata) 
else:
 filedata = filedata.replace('daemon', 'daemon\nnserver {}'.format(nameserver))

with open(filename, 'w') as file:
  file.write(filedata)
