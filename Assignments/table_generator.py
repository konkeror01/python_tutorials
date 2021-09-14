def table_generator(a):
    for i in range(1, 101):
        print(f"{a} x {i} = {a * i}")


number = int(input("Enter a number: "))
table_generator(number)
