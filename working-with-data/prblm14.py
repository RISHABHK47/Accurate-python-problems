#Problem 14: Improve the unique function written in previous problems to take an optional key function as argument
#  and use the return value of the key function to check for uniqueness
def unique(list,key):
    l=[]
    for i in list:
        if key(i) not in l:
            l.append(i)
    return l

print(unique(["python", "java", "Python", "Java"], key=lambda s: s.lower()))