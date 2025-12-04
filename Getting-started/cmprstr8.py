#Write a function istrcmp to compare two strings, ignoring the case.

def istrcmp(x,y):
    if x.upper() == y.upper():
        return True
    else:
        return False
print(istrcmp("hai","HaI"))         #True
print(istrcmp('python', 'Python'))  # True
print(istrcmp('LaTeX', 'Latex'))   # True
print(istrcmp('a', 'b'))         #false
print(istrcmp('fb','gh'))      #false