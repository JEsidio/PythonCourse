#Creating the game function

def game_start():

    print("***************************************");
    print("**** Welcome to the guessing game! ****");
    print("***************************************");

    secret_number = 42;
    guess = int(input("Type your guess number: "));
    right_guess = (guess == secret_number);
    higher_guess = (guess > secret_number);

    print("\nYour guess was: ", guess);

    if (right_guess):
        print("Congratulations! You won!");
    else:
        if (higher_guess):
            print("Sorry. You missed! Your guess was higher than the secret number.")
        else:
            print("Sorry. You missed! Your guess was lower than the secret number.")

    print("\nEnd of the game");