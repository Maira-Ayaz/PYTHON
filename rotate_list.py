#iven a list nums and integer k, rotate the list to the right by k positions.
def rotate(a, b):

    for i in range(b):

        last = a.pop()

        a.insert(0, last)

    return a


print(rotate([12,4,5,7,8], 3))