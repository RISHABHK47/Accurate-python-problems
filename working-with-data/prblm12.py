#Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.
l=[]
def group(list,size):
    for i in range(0,len(list),size):
        l.append(list[i:i+size])
    return l
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))   #[[1,2,3],[4,5,6],[7,8,9]]