# List Methods and Functions Part 4

# This is the sample data :
data = ["kaustubh", "albert", "mark", "kaustubh", "krishna", "alan"]

# some more method to add the data in a list :

# .insert() method
# this method add data to the list at the index to which provide

print(data)
data.insert(2, "simone")
# Syntax of .insert() method -> .insert(index_no, "<element_name>")
print(data)

# .extend() method
# this method fetches all the elements from the list provided and extend with the existing
#...to the list in which it has be extended.

cars1 = ["BMW i8", "Porsche 356", "Rolls Royce"]
cars2 = ["Mercedes C", "Tesla", "Nio", "Xpev"]

# Another method to do the same thing
cars = cars1 + cars2
print(cars)

# Standard Method -> Conventional
# print(cars1)
# cars1.extend(cars2)
# print(cars1)
