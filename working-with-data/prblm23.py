#Write a program center_align.py to center align all lines in the given file.
import sys
file=sys.argv[1]
g=open(file).readlines()
for i in g:
    print(i.center())
    # not completd