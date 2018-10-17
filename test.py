import os
import sys

def new_name(file):
    file='simple.svg'
    os.path.splitext(file)
    return '.'.join([os.path.splitext(file)[0],'jpg'])

files = sys.argv[1:]

for file in files:
    os.system('rsvg %s %s' % (file, new_name(file)))
