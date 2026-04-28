def calculator(a,b,operation):
    if operation=="add":
     return (a+b)
    elif operation=="sub":
       return(a-b)
    elif operation=="mul":
       return(a*b)
    elif operation==("divide"):
       if b==0:
          print("not divisible")
       else: 
          return(a/b)
