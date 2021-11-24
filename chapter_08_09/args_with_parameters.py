def mul_nums(num1, *args):
    multi = 1
    for i in args:
        multi *= i
    return num1, multi


print(mul_nums(1,2,3))

