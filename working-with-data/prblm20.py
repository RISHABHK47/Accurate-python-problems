#problm 20 :Implement unix command grep.
# The grep command takes a string and a file as arguments and
#  prints all lines in the file which contain the specified string.
"""import sys
file=sys.argv[1]
word=sys.argv[2]
grep=open(file).readlines() # this code is used when we take input frm terminal
for i in g:
    if word in i:
           print(i)"""
def grep(filename,string):
    g=open(filename).readlines()
    for i in g:
        if string in i:
            print(i)
grep('reverse.txt',"sure")






