import random
number=random.randint(1,10)
attempt = 0
print("you have 7 chance to guess the number")
for i in range(1,8,1):
    user_number=int(input("enter number between 1 to 10 : "))
    attempt=attempt+1
    if user_number==number:
        print("you guessed right !")
        print("attempts" , attempt)
        break
    elif user_number > number:
        print("Too High")
    else:

        print("Too low")
else:
    ("you lose ! , the number was" , number)

    
    

    
    
 
