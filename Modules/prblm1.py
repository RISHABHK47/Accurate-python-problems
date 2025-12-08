#Problem 1: Write a program to list all files in the given directory.
import os
directory=input("Eneter path of directory:")
print(os.listdir(directory))