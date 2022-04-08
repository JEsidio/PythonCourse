#Creating the game function

def game_start():

    print("***************************************");
    print("**** Welcome to the guessing game! ****");
    print("***************************************");

    secret_number = 42;

    guess = int(input("Type your guess number: "));

    print("\nYour guess was: ", guess);

    if (secret_number == guess):
        print("Congratulations! You won!");
    else:
        print("Sorry. You miss! The right choice was: ", secret_number);

    print("\nEnd of the game");