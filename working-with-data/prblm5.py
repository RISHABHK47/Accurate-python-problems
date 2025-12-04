#Write a function factorial to compute factorial of a number.
#Can you use the product function defined in the previous example to compute factorial?

def product(list):
     mul = 1
     for i in list:
        mul = mul * i
     return mul

def factorial(num):
    numbers = list(range(1, num + 1))
    return product(numbers)
print(factorial(4))      # 24