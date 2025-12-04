#problm 4: Implement a function product, to compute product of a list of numbers.

def product(list):
    mul=1
    for i in list:
        mul=mul*i
    return mul

print(product([1, 2, 3]))    #6