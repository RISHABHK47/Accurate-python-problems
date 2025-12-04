#Implement unix commands head and tail.
#  The head and tail commands take a file as argument
# and prints its first and last 10 lines of the file respectively.

def head(file1):
    f1=open(file1).readlines()
    for i in range(10):
        print(f1[i])
def tail(file1):
    f1=open(file1).readlines()
    for i in range(1,11):
        print(f1[-i])
head('hai.txt')
tail('hai.txt')