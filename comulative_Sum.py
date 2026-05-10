def add_index(a):
    total = 0
    result = []
    for i in a:
        total = total + i
        result.append(total)
    return result
print(add_index([1,4,5,6,7]))
    