# even odd
results=["even" if n % 2==0   else "odd" for n in range(20) ]
print(results)

# square

square = [ n**2 for n in range(6)]
print (square)

# lenght of string
string = ["maira" , "hajra", "abiha" , "maryum"]
lenght = [ strings for strings in string if len(strings)>=6 ]
print(lenght)

# positive number
number = [ 2,5,-9,-200,30]
positve = [ n for n in number if n >=0]
print(positve)

# find vowels
text = "MAIRA"
vowels = [ v for v in text if v  in "aeiouAEIOU"]
print(vowels)

# replace negative numbers with 0
numbers = [4,-9 ,45 , -10 , 8]
result = [ n if n >0 else 0 for n in numbers ]
print(result)
