#print word and associated row number. end game if user press "enter"

word = "nothing"
n = 0

while word != "":
    word = input(str("Type a word or press 'Enter' to end the game: "))
    n += 1
    if word != "":
        print(n, word)
print("Thank you. Goodbye!")

