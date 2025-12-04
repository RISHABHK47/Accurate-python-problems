#Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
# Write a function cumulative_sum to compute cumulative sum of a list.
#  Does your implementation work for a list of strings?

def cumulative_sum(list):
    l=[]
    sum=0
    for i in list:
        if i == list[0]:
            l.append(i)
        else:
            for j in l:
              sum=i+j
            l.append(sum)
    return l
print(cumulative_sum([1, 2, 3, 4]))     #[1,3,6,10]
print(cumulative_sum([4, 3, 2, 1]))     #[4,7,9,10]