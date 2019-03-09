from datetime import datetime
from random import *
import time
import os

i = 0

command = os.popen('snmpget -v2c -c public localhost .1.3.6.1.4.1.30503.1.5.2').read()
result = command.replace('SNMPv2-SMI::enterprises.30503.1.5.2 = STRING: "', '')
next = result.replace('.00"', '')

command = str(next)


def save_to_graph():
    while True:
        global i
        # rad= randint(20, 40)
        # rad=str(rad)

        f = open("./Graphstest2.txt", "a")
        i = str(i)
        f.write(i)
        f.write(",")

        f.write(str(next))
        f.write("\n")

        i = int(i)
        i = i + 1
        f.close()
        time.sleep(1)

if __name__ == '__main__':
    save_to_graph()
