# create a program that sums up 10 first integers. Use while loop to sum up these numbers

sum1 = []
sum= 0

number = 0
#numbers = range(1,11)
while number <=10:
 #   print(number)
    sum += number
    sum1.append(number**2)
    number += 1

print(sum)
print(sum1)

