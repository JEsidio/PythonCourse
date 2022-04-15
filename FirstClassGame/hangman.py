import random;
import unicodedata;
# import re;


def start():
    print_opening_message();

    # level = level_chose();

    number_of_tries = 7; # get_number_of_tries(level);

    secret_word = load_words_file();

    right_letters = ["_" for letter in secret_word];
    all_letters = [];
    hanged = False;
    won = False;
    wrong_tries = 0;

    print(secret_word)

    print("\nThe word you'll have to guess has {} letters and you got {} tries. "
          "Good luck!\n".format(len(right_letters), number_of_tries));

    print_correct_letters(right_letters);

    while (not hanged and not won):

        guess = get_guess(number_of_tries, wrong_tries);

        if (guess in all_letters):
            print("\nYou already typed this letter. You lost 1 try.");
            wrong_tries += 1;

            print_correct_letters(right_letters);

            all_letters = list(dict.fromkeys(all_letters));
            all_letters.sort();

            print_all_letters(all_letters);

            hanged = wrong_tries == number_of_tries;
            won = "_" not in right_letters;

            draw_hangman(wrong_tries);

            continue;

        if (guess in secret_word):
            check_correct_guess(secret_word, guess, right_letters, all_letters);
        else:
            draw_hangman(wrong_tries);
            all_letters.append(guess);
            wrong_tries += 1;

        hanged = wrong_tries == number_of_tries;
        won = "_" not in right_letters;

        print("\n");

        print_correct_letters(right_letters);

        all_letters = list(dict.fromkeys(check_correct_guess(secret_word, guess, right_letters, all_letters)));
        all_letters.sort();

        print_all_letters(all_letters);

    if (won):
        print_winning_message(number_of_tries);
    else:
        print_lose_message(secret_word);

    print_end_message();


"""
def remove_accents_regex(string: str) -> str:
    regex = re.compile(r'[\u0300-\u036F]', flags=re.DOTALL)
    normalized = unicodedata.normalize('NFKD', string)
    return regex.sub('', normalized)
"""


def remove_accents(string: str) -> str:
    normalized = unicodedata.normalize('NFKD', string)
    return ''.join([c for c in normalized if not unicodedata.combining(c)])


def print_opening_message():
    print("***************************************");
    print("******* Welcome to the Hangman! *******");
    print("***************************************\n");


def level_chose():
    level = 0;
    while not (level in range(1, 4)):
        print("Choose a difficulty level to try to hit the secret number:");
        print("*************** 1-Easy | 2-Medium | 3-Hard ***************");
        level = int(input());
        return level;


def get_number_of_tries(lev):
    if (lev == 1):
        number_of_tries = 20;
    elif (lev == 2):
        number_of_tries = 15;
    else:
        number_of_tries = 10;
    return number_of_tries;


def load_words_file():
    with open("words.txt", "r", encoding='utf-8') as file:
        words_list = [];
        for line in file:
            normalized_word = remove_accents(line);
            words_list.append(normalized_word.strip().upper());

    """
    file = open("words.txt", "r", encoding='utf-8');
    words_list = [];
    for line in file:
        normalized_word = remove_accents(line);
        words_list.append(normalized_word.strip().upper());
    file.close();
    """

    number_of_words = random.randrange(0, len(words_list));
    secret_word = words_list[number_of_words];
    return secret_word;


def print_correct_letters(right_letters):
    for character in right_letters:
        print(character, sep=" ", end=" ");


def print_all_letters(all_letters):
    print("\nAlready typed letters: ", end="")
    for character in all_letters:
        print(character, sep="-", end=" ");


def get_guess(number_of_tries, wrong_tries):
    guess = input("\n\nTries left: {}. Please, type a letter: ".format(number_of_tries - wrong_tries));
    guess = guess.strip().upper();
    return guess;


def check_correct_guess(secret_word, guess, right_letters, all_letters):
    index = 0;
    for letter in secret_word:
        if (guess == letter):
            right_letters[index] = letter;
            all_letters.append(guess);
        index += 1;
    return all_letters;


def draw_hangman(wrong_tries):
    print("  _______     ")
    print(" |/      |    ")

    if (wrong_tries == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (wrong_tries == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (wrong_tries == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (wrong_tries == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (wrong_tries == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (wrong_tries == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (wrong_tries == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_winning_message(number_of_tries):
    print("\n\n\nCongratulations! You won with this total of tries: {}!".format(number_of_tries));
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_lose_message(secret_word):
    print("\n\n\nSorry! You got hanged..")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_end_message():
    print("\n****************************************");
    print("*********** End of the game! ***********");
    print("****************************************");



if (__name__ == "__main__"):
    start();
