#problem 6 :Write a function reverse to reverse a list. Can you do this without using list slicing?

def reverse(list):
    r=[]
    for i in reversed(list):
        r.append(i)
    return r

print(reverse([1, 2, 3, 4]))   #[4,3,2,1]
print(reverse(reverse([1,2,3,4])))  #[1,2,3,4]