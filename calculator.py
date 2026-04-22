def calculator(a,b,operation):
    if operation=="add":
     return (a+b)
    elif operation=="sub":
       return(a-b)
    elif operation=="mul":
       return(a*b)
    elif operation==("divide"):
       if b==0:
          return"not divisible"
       return(a/b)
print(calculator(9,0,"sub"))
print(calculator(10,8,"mul"))
print(calculator(8,0,"divide"))
print(calculator(10,8,"add"))
