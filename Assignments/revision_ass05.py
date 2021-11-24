"""
Insert your name : bob boxer

b : 3
o : 2
  : 1
x : 1
e : 1
r : 1
"""

name = "Albert ALove"

var = ""
i = 0

while i < len(name):
    if name[i] not in var:
        var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1

# #counter = []
#
# for i in range(0, len(name)):
#    # counter.append(i)
#     if name.count(name[i]) >= 2:
#         continue
#     else:
#         print(name[i], " ", name.count(name[i]))
#
#     i = i + 1
