import random

min = 0
max = 3 #user hanya diizinkan untuk menebak angka hanya 3 kali

random_number = random.randint(0, 100)

for min in range(max):
    number_user = int(input("Input your number (0-100) : "))

    if number_user > 100:
        print("Number should be between 0 - 100. Please input again")

    elif number_user > random_number:
        print("Your guess is too high, Please input again")
    elif number_user < random_number:
        print("Your guess is too low, Please input again")
    else :
        print("Congratulations, your guess number is correctly")
    
else :
    print(f"Sorry, you lost! The correct number was {random_number}")
