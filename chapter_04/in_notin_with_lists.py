cars1 = ["BMW i8", "Porsche 356", "Rolls Royce"]

user_input = input("Insert: ")

# if user_input in cars1:
#     print(f"{user_input} car available in stock.")
# else:
#     print(f"{user_input} car is not available in stock.")

if user_input not in cars1:
    print(f"{user_input} is not car available in stock.")
else:
    print(f"{user_input} car is available in stock.")
