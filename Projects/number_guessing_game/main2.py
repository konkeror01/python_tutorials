"""You will have a winning_number variable in your python script For an eg. winning_number = 8
If the number is more than 8, it should spit out 'Its high'.
If the number is less than 8, it should spit out 'Its low'.
If the number = 8, it should say 'You win.'
If the number is either less than 1 or more than 100 then it should print out 'Its not expected.'
"""

winning_number = 8
user_input = int(input("Can you guess the winning number? "))
while user_input != winning_number:
    if winning_number < user_input <= 100:
        print("Number is too high")
    elif winning_number >user_input >1:
        print("Number is too low")
    elif user_input > 100 or user_input <1:
        print("It's not expected")
    user_input = int(input("Can you guess the winning number? "))
else:
    print("Congratulations you won!")