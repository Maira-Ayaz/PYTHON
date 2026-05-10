def common(a, b):
    result = []

    for i in a:
        if i in b and i not in result:
            result.append(i)

    return result


print(common([1,2,3], [2,4,3])) 
        