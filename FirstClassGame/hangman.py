import random;
import unicodedata;
##import re;


"""
def remove_accents_regex(string: str) -> str:
    regex = re.compile(r'[\u0300-\u036F]', flags=re.DOTALL)
    normalized = unicodedata.normalize('NFKD', string)
    return regex.sub('', normalized)
"""


def remove_accents(string: str) -> str:
    normalized = unicodedata.normalize('NFKD', string)
    return ''.join([c for c in normalized if not unicodedata.combining(c)])


def start():
    print("***************************************");
    print("******* Welcome to the Hangman! *******");
    print("***************************************\n");

    file = open("words.txt", "r", encoding='utf-8');
    words_list = [];
    for line in file:
        normalized_word = remove_accents(line);
        words_list.append(normalized_word.strip().upper());
    file.close();

    number_of_words = random.randrange(0, len(words_list));
    secret_world = words_list[number_of_words];
    right_words = ["_" for letter in secret_world];
    hanged = False;
    won = False;
    wrong_tries = 0;

    print(right_words)

    while (not hanged and not won):

        guess = input("Letter?");
        guess = guess.strip().upper();
        index = 0;

        if (guess in  secret_world):
            for letter in secret_world:
                if (guess == letter):
                    right_words[index] = letter;
                index += 1;
        else:
            wrong_tries += 1;

        hanged = wrong_tries == 15;
        won = "_" not in right_words
        print(right_words)

    if (won):
        print("Won")
    else:
        print("Lose")

    print("\n****************************************");
    print("*********** End of the game! ***********");
    print("****************************************");

if (__name__ == "__main__"):
    start();