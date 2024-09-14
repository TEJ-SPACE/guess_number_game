'''
"Guess the Number" game!
The computer randomly selects a number between 1 and 100. 
The player then has to guess the number in as few attempts as possible. 
After each guess, the computer tells the player whether their guess is too high or too low. 
The game continues until the player guesses the correct number.
'''

import random

user_num = int(input("Enter your guess between 1 and 100: "))

def guess_number(user_num):
    computer_num = random.randint(1, 100)
    count = 0

    while(user_num != computer_num):
        if user_num <= (computer_num/4):
            print(f"{user_num} is way too low!")
            user_num = int(input("Enter your guess again: "))
            count += 1
        elif user_num <= (computer_num/2) and user_num > (computer_num/4):
            print(f"{user_num} is too low!")
            user_num = int(input("Enter your guess again: "))
            count += 1
        elif user_num < computer_num and user_num > (computer_num/2):
            print(f"{user_num} is low, but you're close!")
            user_num = int(input("Enter your guess again: "))
            count += 1
        elif user_num >= (computer_num*4):
            print(f"{user_num} is way too high!")
            user_num = int(input("Enter your guess again: "))
            count += 1
        elif user_num >= (computer_num*2) and user_num < (computer_num*4):
            print(f"{user_num} is too high!")
            user_num = int(input("Enter your guess again: "))
            count += 1
        elif user_num > computer_num and user_num < (computer_num*2):
            print(f"{user_num} is high, but you're close!")
            user_num = int(input("Enter your guess again: "))
            count += 1

    if user_num == computer_num:
        print(f"You got it! {user_num} is indeed the right answer!")
        count += 1

    return count 

a = guess_number(user_num) # calls function and stores its return value in variable a
print(f"It took you {a} tries to guess it right.")


        
