str=input("Enter a string:")
def replace(string):
      rep=""
      for i in string:
        if i == "s":
            rep=rep+"*"
        else:
            rep=rep+i               #program without replace
      print(rep)
replace(str)



