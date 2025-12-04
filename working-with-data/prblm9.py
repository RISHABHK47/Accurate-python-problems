#problem 9 cummilative_product

def cumulative_product(list):
    l=[]
    product=1
    for i in list:
        if i == list[0]:
            l.append(i)
        else:
            for j in l:
              product=i*j
            l.append(product)
    return l
print(cumulative_product([1, 2, 3, 4]))  #[1, 2, 6, 24]
print(cumulative_product([4, 3, 2, 1]))    #[4, 12, 24, 24]