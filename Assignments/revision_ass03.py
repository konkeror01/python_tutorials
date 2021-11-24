"""
Insert the number : 11
66
"""
number = int(input("Insert an integer: "))
total = 0
i = 0
# for i in range(1, number + 1):
#     total += i
# print(total)

while i <= number:
    total += i
    i = i + 1

print(total)

