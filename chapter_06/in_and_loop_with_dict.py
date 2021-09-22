user_info = dict(
    name="Albert Nzayisenga",
    age=32,
    fav_movies=["game of thrones", "Wakanda", "Troy"],
    fav_players=["Kobe Bryant", "Magic Johnson", "Lionel Messi"]
)

# check if key exists in the dictionary or not :
if "name" in user_info:
    print("present")
else:
    print("Not Present")

# check if value exists in the dictionary or not :
if 32 in user_info.values():
    print("present")
else:
    print("Not Present")

for i in user_info:
    print(i)

for i in user_info.values():
    print(i)