#Problem 17: Write a program reverse.py to print lines of a file in reverse order
import sys
file_name=sys.argv[1]
lines = open(file_name).readlines()
print(*lines[::-1])
