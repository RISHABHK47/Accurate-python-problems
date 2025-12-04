#Problem 10: Write a function unique to find all the unique elements of a list.
def unique(list):
    l=[]
    for i in list:
        if i not in l:
            l.append(i)
    return l
print(unique([1, 2, 1, 3, 2, 5]))     #[1,2,3,5]