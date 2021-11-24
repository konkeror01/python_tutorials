# def add_number(a,b):
#     return a+b
#
#
# print(add_number(4,5,6,7))

# *args

def func(*args):
    total = 0
    i = 0
    print(args)
    while i < len(args):
        total += args[i]
        i = i+1
    print(total)

    # print(sum(args))

func(1,2,3,4,5,6,7,8,9,10)


