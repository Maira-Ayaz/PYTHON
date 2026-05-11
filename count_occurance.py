#Given a list nums and a value target, return how many times target appears in nums without using
#list.count().

def find_num( number , target):
    count = 0 
    for num in number:
        if num == target:
            count = count + 1 
    return count 
print (find_num([1,2,2,2,3,4] , 2))


    