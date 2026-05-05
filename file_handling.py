with open("my_info","w") as file:
    file.write("Iam learning python")
with open("my_info","r") as file:
    print(file.read())
with open("my_info","a") as file:
    file.write("i will master python soon")
with open("my_info","r") as file:
    print(file.read())

