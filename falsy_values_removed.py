#Given a list items, return a new list with all falsy values (None, 0, False, '', []) removed.
def remove_falsy(items):
    result = []

    for i in items:
        if i:
            result.append(i)

    return result


print(remove_falsy([0, 1, False, "Ali", "", None, [], [1,2]]))
            
            