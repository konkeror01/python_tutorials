# kwargs -> Kaustubh Wankehde Arguments -> JFF
# kwargs -> Keyword Arguments

# *args -> star operator
# **kwargs -> double star operator.

def func(**kwargs):
    # kwargs = {"a": 1, "b": 2, "c": 3}
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


func(a=1, b=2, c=3)

data = dict(
    first_name = "Albert",
    last_name = "Nzayisenga",
    age = 32,
    country = "Switzerland"
)

func(**data)
