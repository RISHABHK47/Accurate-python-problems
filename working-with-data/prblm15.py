#Problem 15: Reimplement the unique function implemented in the earlier examples using sets.
def unique(sets):
    s=set([])
    for i in sets:
        if i not in s:
            s.add(i)
    return s
print(unique(set([3,1,2,3,1])))  #{1,2,3}