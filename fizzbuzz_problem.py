#Given an integer n, return a list of strings from 1 to n where multiples of 3 are 'Fizz', multiples of 5 are
#'Buzz', and multiples of both are 'FizzBuzz'.

def multiples(n):
    result = []
    
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                result.append("FizzBuzz")
            else:
                result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    
    return result
print(multiples(7))