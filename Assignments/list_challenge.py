items = []
n_items = int(input("How elements to you want? :"))

for i in range(1, n_items+1):
    item = input(f"Insert no {i}:")
    items.append(item)

print("the list combined is:", items)
