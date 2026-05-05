def merge_dict(d1,d2):
    result={}
    for key in d1:
       result[key] = d1[key]
    for key in d2:
       result[key] = d2[key]

    return result

print(merge_dict({"a": 8, "b": 2}, {"a": 1, "b": 3, "c": 4}))