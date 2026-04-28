import calculator

while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Choose operation: add / sub / mul / divide")
    op = input("Enter operation: ")

    result = calculator.calculator(num1, num2, op)#file name and function name
    print("Result:", result)

    again = input("Do you want to continue? (yes/no): ").lower()

    if again == "no":
        break