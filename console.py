from dumpster import Dumpster
import os

running = True
selected = ''

while running:
    #cwd = os.getcwd()

    i = input('\r%s>'%(selected))

    if i == 'exit':
        running = False

    if i[0:6] == 'create':
        name = input('name: ')
        size = input('size: ')
        Dumpster(name, size).write_to_dump()

    if i == 'list':
        if selected is '':    #list currrent working directory
            dirs = ''
            lcd = os.listdir()
            for file in lcd:
                if '.dmp' in file:
                    dirs+= ' '+file.strip('.dmp')
            print(dirs)

        else:                 #list selected dump
            pass

    if i[0:6] == 'select':
        name = i[7:]
        selected = name
