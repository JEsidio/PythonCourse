import guessing;
import hangman;


def chose_game():
    print("**************************************");
    print("************** Welcome! **************");
    print("**************************************\n");

    game = 0;

    while not (game in range(1, 3)):
        print("Choose the game you want to play:")
        print("1-Guessing: Try to guess the secret number within a certain number of guesses.")
        print("2-Hangman: Try to guess a phrase or sentence by suggesting letters within a certain number of guesses.")
        game = int(input())

    if (game == 1):
        guessing.start();
    elif (game == 2):
        hangman.start();

if (__name__ == "__main__"):
    chose_game();


