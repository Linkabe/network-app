import subprocess
import os
f = os.popen('FOR /L %i IN (1,1,2) DO ping -n 1 192.168.0.%i | FIND "TTL="')
for line in f:
    line = line.strip()
    r = open("./logfile.txt", "a+")
    r.write(line + "\n")
    r.close()
f.close()
open('./logfile.txt', 'r').read().find('Reply')
if True:
    print(True)

