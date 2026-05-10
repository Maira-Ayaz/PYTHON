def temp(a, b):
    if b == "C":
        return a * 9/5 + 32
    else:
        return (a - 32) * 5/9


print(temp(25, "C"))   
print(temp(77, "F"))   