l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = [5, 7, 8, 9, 6]

# == -> checks the values in the list
print(l1 == l2)  # True
print(l1 == l3)  # False

# is -> checks the memory allocation
print(l1 is l2)  # False
print(l1 is l3)  # False
