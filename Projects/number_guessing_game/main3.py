# Here are the imports / dependencies for this project.
from random import randint

"""You will have a winning_number variable in your python script For an eg. winning_number = 8
If the number is more than 8, it should spit out 'Its high'.
If the number is less than 8, it should spit out 'Its low'.
If the number = 8, it should say 'You win.'
If the number is either less than 1 or more than 100 then it should print out 'Its not expected.'
"""
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

easy_attempts = 15 #number of lives for easy level
easy_lives = 0
hard_attempts = 10 #number of lives for hard level
hard_lives = 0
winning_number = randint(1,100)


user_level = str(input("Choose a difficulty. Type 'easy' or 'hard':").casefold())
#this section will run if user Choose option "easy"
if user_level == "easy":
    print(f"You have {easy_attempts} attempts")
    while easy_lives < easy_attempts:
        user_input = int(input("Can you guess the winning number? "))
        if winning_number < user_input <= 100:
            print("Number is too high")
        elif winning_number >user_input >1:
            print("Number is too low")
        elif user_input > 100 or user_input <1:
            print("It's not expected")
        elif user_input ==winning_number:  
            print("Congratulations you won!")
            easy_lives = easy_attempts #end game if user guesses correctly
        else: 
            print("Sorry! You failed")
        easy_lives += 1 #keep running until max lives are attained

#this section will run if user Choose option "hard"
if user_level == "hard":
    print(f"You have {hard_attempts} attempts")
    while hard_lives < hard_attempts:
        user_input = int(input("Can you guess the winning number? "))
        if winning_number < user_input <= 100:
            print("Number is too high")
        elif winning_number >user_input >1:
            print("Number is too low")
        elif user_input > 100 or user_input <1:
            print("It's not expected")
        elif user_input == winning_number:
            print("Congratulations you won!")
            hard_lives = hard_attempts #end game once user guesses winning number
        else:
            print("Sorry! You failed")
        hard_lives += 1 #keep running until max lives are attained

