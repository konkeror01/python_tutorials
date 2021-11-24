import numpy
import numpy as np

# should take multiple parameters and multiply them
def multiply_numbers(*args):
    # ([1,2,3,4,5],)
    # [1,2,3,4,5]
    mult = 1
    # i = 0
    # while i < len(args):
    #     mult *= args[i]
    #     i += 1
    # print(mult)

    # for i in range(len(args)):
    #     mult *= args[i]
    #     i += 1
    # print(mult)

    for i in args:
        mult *= i
    print(mult)

    print(numpy.prod(args))

# sum()

data = [3,4,5,6,7]



multiply_numbers(data)
multiply_numbers(*data)
multiply_numbers(2,3,4)

# def add_2_nums(a,b):
#     return a+b
#
# print(add_2_nums(3,4))
#
# def add_2_nums_func(a,b):
#     print(a+b)
#
# add_2_nums_func(3,4)
