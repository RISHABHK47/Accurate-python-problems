#Problem 16: Write a function extsort to sort a list of files based on extension


def extsort(list):
    for i in list:
        list.sort(key=lambda x:x.split('.')[-1])
    return list
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))