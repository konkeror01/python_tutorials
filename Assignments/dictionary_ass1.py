user_info = dict(
    name="Albert Nzayisenga",
    age=32,
    fav_movies=["game of thrones", "Wakanda", "Troy"],
    fav_players=["Kobe Bryant", "Magic Johnson", "Lionel Messi"]
)

# for i in user_info.items():
#     print(i)


for i in user_info.items():
    key, value = i
    print(key, "=", value)

"""
name="Albert Nzayisenga",
age=32,
fav_movies=["game of thrones", "Wakanda", "Troy"],
fav_players=["Kobe Bryant", "Magic Johnson", "Lionel Messi"]
"""
