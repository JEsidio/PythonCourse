import random;


def start():

    print("***************************************");
    print("**** Welcome to the guessing game! ****");
    print("***************************************\n");

    secret_number = random.randrange(1, 101);
    level = 0;
    points = 1000;

    while not (level in range(1, 4)):
        print("Choose a difficulty level to try to hit the secret number:")
        print("*************** 1-Easy | 2-Medium | 3-Hard ***************")
        level = int(input())

    if (level == 1):
        number_of_tries = 20;
    elif (level == 2):
        number_of_tries = 10;
    else:
        number_of_tries = 5;

    print("\nNumber of tries: {}. Good luck!".format(number_of_tries));

    print("\nAttention: the secret number always will be a positive number between 1 and 100, "
          "so your guess must be in this range.\n");

    for current_try in range(1, number_of_tries + 1):
        print("Try: {} of {}".format(current_try, number_of_tries));
        guess = int(input("Type your guess number: "));
        right_guess = (guess == secret_number);
        higher_guess = (guess > secret_number);

        if (guess < 1 or guess > 100):
            print("You entered a number, {}, out of the guess range. Sorry, you lost one try.\n".format(guess));
            continue;

        if (right_guess):
            print("\nCongratulations! You won and made {} points of 1000!\n".format(points));
            break;
        else:
            if (higher_guess):
                print("\nSorry. You missed! Your guess was higher than the secret number.\n")
            else:
                print("\nSorry. You missed! Your guess was lower than the secret number.\n")
            lost_points = abs(secret_number - guess);
            points = points - lost_points;

    print("\n****************************************");
    print("*********** End of the game! ***********");
    print("****************************************");

if (__name__ == "__main__"):
    start();