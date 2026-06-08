#Given a list of integers nums and an integer target, return indices of the two numbers that add up to target. Each input has exactly one solution; you may not use the same element twice.
def sum_index(a, b):
    d = {}

    for i in range(len(a)):
        need = b - a[i]

        if need in d:
            return d[need], i

        d[a[i]] = i

print(sum_index([2, 3, 4, 5], 8))
