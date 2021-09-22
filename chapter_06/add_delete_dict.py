user_info = dict(
    name="Albert Nzayisenga",
    age=32,
    fav_movies=["game of thrones", "Wakanda", "Troy"],
    fav_players=["Kobe Bryant", "Magic Johnson", "Lionel Messi"]
)

# Add data to the dictionary :
user_info["address"] = "123 Street, Switzerland"

print(user_info)

# pop()
user_info.pop("fav_movies")
print(user_info)

# popitem method:
user_info.popitem()
print(user_info)
