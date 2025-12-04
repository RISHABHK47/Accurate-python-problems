
numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    print(numcalls)
    return x * x
#problem 2
print(square(5))
print(square(2*5))

#problem 3
x = 1
def f():
    return x
print(x)
print(f())

#problem 4
x = 1
def f():
    x = 2
    return x
print(x)
print(f())
print(x)

# #problem 5
# x = 1
# def f():
#         y = x      # ERROR
#         x = 2
#         return x + y
# print(x)
# print(f())
# print(x)

#problem 6
x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x, y)

# using Anonymous function lambda
cube = lambda x: x ** 3
f= cube
def fxy(f, x, y):
    return f(x) + f(y)
print(fxy(f, 2, 3))
z=square
print(fxy(z,3,4))

#7 problm : Write a function count_digits to find number of digits in the given number
def count_digits(x):
    return len(str(x))
print(count_digits(24))
print(count_digits(123456))

#Problem 8: Write a function istrcmp to compare two strings, ignoring the case.
def istrcmp(x,y):
    if x.upper() == y.upper():
        return True
    else:
        return False
print(istrcmp("hai","HaI"))
print(istrcmp('python', 'Python'))
print(istrcmp('LaTeX', 'Latex'))
print(istrcmp('a', 'b'))
print(istrcmp('fb','gh'))


for x in [1, 2, 3, 4]:
    print(x)

for i  in range(10):
   print(i, i*i, i*i*i)