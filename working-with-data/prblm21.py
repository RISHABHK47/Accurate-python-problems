#Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys
file=sys.argv[1]
width=int(sys.argv[2])
def wrap(file,width):
    with open(file) as f:
        for i in f:
            w=width
            while len(i)>width:
                print(i[:w])
                i=i[w:]
            print(i,end="")
wrap(file,width)
