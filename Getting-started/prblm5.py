x = 1
def f():
        y = x     #ERROR : cannot access local variable
        x = 2
        return x + y
print(x)
print(f())
print(x)