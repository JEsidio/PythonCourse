#Creating the game function

def game_start():

    print("***************************************");
    print("**** Welcome to the guessing game! ****");
    print("***************************************\n");

    number_of_tries = 0;

    while not (number_of_tries in range(1, 10)):
        number_of_tries = int(input("\nHow many tries would you like to have? (Type a number between 1 and 10): "))

    current_try = 1;
    secret_number = 42;

    print("\nNumber of tries: {}. Good luck!\n".format(number_of_tries));

    while (current_try <= number_of_tries):
        print("Try: {} of {}".format(current_try, number_of_tries));
        guess = int(input("Type your guess number: "));
        right_guess = (guess == secret_number);
        higher_guess = (guess > secret_number);

        if (right_guess):
            print("\nCongratulations! You won!\n");
            break;
        else:
            if (higher_guess):
                print("\nSorry. You missed! Your guess was higher than the secret number.\n")
            else:
                print("\nSorry. You missed! Your guess was lower than the secret number.\n")

        current_try = current_try + 1;

    print("\n****************************************");
    print("*********** End of the game! ***********");
    print("****************************************");