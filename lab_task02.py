#task no 01
name="maira"
age=21
city="rawlpindi"
print("my name is ",name)
print("my age is ",age)
print("i live in",city)

#task02
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("addition is ",num1+num2)
print("substraction",num1-num2)
print("multiplication",num1*num2)
print("division",num1/num2)

#task03
num = int(input("Enter  number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")


#task04

marks = int(input("Enter  marks: "))
if marks >=90 :
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

#task05
n=int(input("enter number"))
for i in range(1,11) :
    print(print(n, "x", i, "=", n * i))

#task06
total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

#task07
list=["apple","mango","guava","orange","banana"]
print(list)
list.append("melon")
list.remove("mango")
print("updated lits",list)

#task08
password=(input("enter password"))
if password == "python123":
    print("access granted")
else:
    print("access denied")

#task09
def square(a):
    return(a**2)
result=square(4)
print("square of 4 is", result)

#task10
total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

# Calculate percentage
percentage = (attended_classes / total_classes) * 100

print("Attendance Percentage:", percentage, "%")

# Check eligibility
if percentage >= 75:
    print("Allowed in Exam")
else:
    print("Not Allowed")

#task11
secret=7
n=int(input("enter number to guess"))
if n == secret :
    print("you won !")
else:
    print("you lost")


