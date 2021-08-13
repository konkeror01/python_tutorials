age = int(input("Insert your age : "))

# If the age of the person is less than 18 then we will go ahead and print out that you are not eligible for voting.
# If that's not the case then we will go ahead and print out you are eligible for voting.

# if age < 18:  # Boolean Expression -> That we receive an answer in yes or no / True or False
#     print("You are not eligible for voting.")


# 1 indentation = 1 tab = 4 spaces

# This was some text added to explain git functionality
# if age >= 18:
#     print("You are eligible for voting.")

# else:
#     print("You are eligible for voting.")

if age > 18:
    print("You are able to work.")

# = -> assignment operator
# == -> check operator
# elif is a short abbreviation of else if.
elif age == 18:
    print("You are able to work")

else:
    print("You are not able to work.")
