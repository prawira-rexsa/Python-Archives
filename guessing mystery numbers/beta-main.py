import random

# min = 0
# max = 3 #user hanya diizinkan untuk mencoba 3x saja

random_number = random.randint(0, 100)

while True:
    number_user = int(input("input your number (0-100) :  "))

    if number_user > 100:
       print("Number should be between 0 and 100. Please input again.")

    elif number_user == random_number:
        print("seri!")
        break
    elif number_user > random_number:
        print("You Win!")
        print(f"{number_user} > {random_number}")
        break
    elif number_user < random_number:
        print("you lose!")
        print(f"{number_user} < {random_number}")
        break
   
print("End Program")
    
    

