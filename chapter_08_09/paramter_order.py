def func(first_name, *args, last_name = "unknown", **kwargs):
    print(first_name)
    print(last_name)
    print(args)
    print(kwargs)

# Normal Parameters
# *args
# Default Parameters
# **kwargs

func("Kaustubh", 1,2,3,4,5,6, x=1, y=2, z=3)
