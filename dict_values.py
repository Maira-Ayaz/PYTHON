#Given a list of keys and a default value, return a dictionary where each key maps to the default value
def dict_values(keys, default):

    result = {}

    for i in keys:
        result[i] = default

    return result


print(dict_values(['a', 'b', 'c'], 0))