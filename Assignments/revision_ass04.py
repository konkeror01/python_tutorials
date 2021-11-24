"""
Insert the number : 1256
14
"""

number = str(input("Insert the number: "))
#print(number[0])
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i = i+1

print(total)
