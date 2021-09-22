# Sets : Unordered collection of unique elements.
# They are declared using curly brackets.
# Sets are not at all dynamic.
# We can store data types not data structures.
# No Indexing.
# Sets are mostly used to remove duplicates.

set1 = {1, 2, 3, 4, 4}
# print(set1)
#
# print(set([1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9]))

set2 = {3, 4, 5, 6, 7}
set2.add(1)
set2.add(0)
print(set2)
# set2.clear()
# print(set2)

# set2.remove(12)
# print(set2)
set2.discard(12)
print(set2)

set3 = set2.copy()
print(set3)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# union
union_set = s1 | s2  # pipe
print(union_set)

# intersection
int_set = s1 & s2  # common
print(int_set)
