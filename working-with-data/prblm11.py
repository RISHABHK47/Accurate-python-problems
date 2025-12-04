#Problem 11: Write a function dups to find all duplicates in the list
def dups(list):
    l=[]
    d=[]
    for i in list:
        if i not in l:
            l.append(i)
        else:
            d.append(i)
    return d
print(dups([1, 2, 1, 3, 2, 5]))    #[1,2]