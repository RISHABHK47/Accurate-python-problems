#Write a program to print each line of a file in reverse order.
import sys
filename=sys.argv[1]
lines = open(filename).readlines()
for i in lines:
       print(i[::-1])

