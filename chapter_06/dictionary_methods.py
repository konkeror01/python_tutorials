# Fromkeys
# d = {
#     "name": "unknown",
#     "age": "unknown"
# }

d = dict.fromkeys(["name", "age"], "unknown")
print(d)

# A fetch data method
print(d["name"])  # no error
# print(d["names"])  # error

# Get Method
print(d.get("name"))
print(d.get("names"))

if d.get("name"):
    print("present")
else:
    print("Not Present")

# Clear
d.clear()  # Empty the Dictionary
print(d)

# Copy
d2 = d.copy()
print(d2)
