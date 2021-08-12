price = input("What's the total bill?")
print(f"Sir, your open invoice is ${price}.")
tip = float(input("how much do you want to tip...$10, $15, $20.5?\n"))
total_price = float(price) + tip
print("Your new total bill is\n", total_price)
people = float(input("How many people will divide the bill?\n"))
price_person = round((total_price / people), 2)
print(f"Alright, that will be ${price_person} per person.")
