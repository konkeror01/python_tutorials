# 1. Write a program that return elements that are common to the list (in other words intersection)
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, "albert"]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "albert"]
c = []
for element in a:
    # print(element)
    if element in b:
        c.append(element)
print(c)
'''

''''
# 2. Reverse a given list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, "albert"]
b = a[::-1]
print(b)
'''

#concanate 2 list index-wise

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:

        c.append(i, j)
print(c)
