def start():
    print("***************************************");
    print("******* Welcome to the Hangman! *******");
    print("***************************************\n");

    secret_world = "banana";
    right_words = ["_", "_", "_", "_", "_", "_"];
    hanged = False;
    won = False;

    print(right_words)

    while (not hanged and not won):

        guess = input("Letter?");
        guess = guess.strip();
        index = 0;

        for letter in secret_world:
            if (guess.upper() == letter.upper()):
                right_words[index] = letter;
            index = index + 1;

        print(right_words)


    print("\n****************************************");
    print("*********** End of the game! ***********");
    print("****************************************");

if (__name__ == "__main__"):
    start();