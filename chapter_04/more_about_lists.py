# Creating a list using a range function

# [1,2,3,4,5,6,7,8,9,10]
"""
list using range()
new_list = list(range(1, 11))
print(new_list)
"""
from future.types import newlist

"""
list using for loop
newlist1 = []
for i in range(1, 11):
    newlist1.append(i)
print(newlist1)
"""

# while i <= 10:
#     print("Hello, World!", i)
#     i = i + 1

i = 1
newlist2 = []
while i <= 10:
    newlist2.append(i)
    i += 1
print(newlist2)
