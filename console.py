from dumpster import Dumpster
import os

i = input('\r>')

if i == 'list':
    cwd = os.getcwd()
    lcd = os.listdir()
    dump = ''
    for file in lcd:
        if '.dmp' in file:
            dump+= ' '+file

    print(dump)
