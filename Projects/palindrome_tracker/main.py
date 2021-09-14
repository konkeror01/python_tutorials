def palindrome_tracker (name):
    if name == name[-1::-1]:
        print("yes, it is")
    else:
        print ("it's not one")
name = input("Type a random word ")
palindrome_tracker(name)

