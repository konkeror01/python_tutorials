play_again = True

while play_again: 
    game_over = False
    while not game_over: #False
    # game_over = True
    # while game_over:
        number = int(input("Guess a number : "))
        if number == 10:
            print("You win")
            game_over = False
            play_again = input("Do you want to play again : ")
            if play_again == "y":
                play_again = True
            else:
                play_again = False
        else:
            if number < 10:
                print("Its Low")
            else:
                print("Its High")