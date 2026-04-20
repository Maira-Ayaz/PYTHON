#Given a list of numbers, remove all duplicate values without using set().
n = [2, 19, 6, 7, 19]
n.sort()

unique = [n[0]]   # make it a list 

for i in range(1, len(n)):
    if n[i] != n[i-1]:
        unique.append(n[i])

print(unique)

#Take a string and count how many vowels and consonants it contains.
s = "Hello World"
vowels = 0
consonants = 0
for char in s:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():  # Check if it's a consonant (i.e., an alphabetic character that is not a vowel)
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

#Check whether a number is a prime number using loops and conditionals.

num = 29
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#Given a list of tuples [(Ali,23),(Sara,19),(John,25)], print the youngest person's name.
people = [("Ali", 23), ("Sara", 19), ("John", 25)]
youngest = min(people, key=lambda x: x[1])
print("The youngest person is:", youngest[0])#returns name

# Create a dictionary from a list like ['a','b','a','c','b'] → {'a':2,'b':2,'c':1}.
lst = ['a', 'b', 'a', 'c', 'b']
count_dict = {}
for item in lst:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)