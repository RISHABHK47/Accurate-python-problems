#Problem 13: Write a function lensort to sort a list of strings based on length.
def lensort(list):
    for i in list:
        list.sort(key=lambda x:len(x))
    return list

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))