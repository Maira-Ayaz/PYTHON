#Given a list of integers nums, return a list of strings 'odd' or 'even' corresponding to each element.
def even_odd(nums):
    list = []
    for num in nums:
        if num % 2 == 0:
            list.append("even")
        else:
            list. append("odd")
    return list
print(even_odd([1,2,4,6,7,9]))
