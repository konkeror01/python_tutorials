# Given two integer numbers return their product.
# If the product is greater than 1000, then return their sum
x1 = int(input("Enter 1st Number: "))
x2 = int(input("Enter 2nd Number: "))
product = x1 * x2
if product > 1000:
    print("Here's the sum: ",x1 + x2)
else:
    print( "Here's the product: ",product)
