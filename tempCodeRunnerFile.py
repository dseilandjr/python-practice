our_number = 42
is_guessed = False

while not is_guessed:
    guess = int(input("Enter an integer: "))
    if guess == our_number:
        print("Hooray!")
        is_guessed = True
    elif guess > our_number:
        print("Too high!")
    else:
        print("Too low")
