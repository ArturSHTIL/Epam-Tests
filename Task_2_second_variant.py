import random
import sys

words = (
    "волдырь", "песок", "лиана", "велосипед", "батискаф", "чернобыль", "повадырь", "лексикон", "амплуа",
    "персонализация",
    "валерьянка", "фантомас", "эверест")


class HangmanGameState:
    def __init__(self):
        self.letters = []
        self.mistakes = 0
        self.secret_word = random.choice(words)
        self.visual_word = ['_'] * len(self.secret_word)


def get_user_input(game_state: 'HangmanGameState') -> str:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    while True:
        print("My word is :", ''.join(game_state.visual_word))
        user_letter = input('insert the letter please: ').lower()
        print()
        if user_letter in alphabet and len(user_letter) == 1:
            if user_letter not in game_state.letters:
                game_state.letters.append(user_letter)
                break
            else:
                print('This letter has already been entered')
                print()
                continue
        else:
            print("Sorry You need entered 1 Russian letter")
            print()

    return user_letter


def is_game_finished(game_state: 'HangmanGameState') -> bool:
    return '_' not in game_state.visual_word or game_state.mistakes >= 10


def handle_user_input(game_state, letter) -> None:
    if letter in game_state.secret_word:
        for ind, value in enumerate(game_state.secret_word):
            if value == letter:
                game_state.visual_word[ind] = letter
    else:
        game_state.mistakes += 1
        print("My word is :", ''.join(game_state.visual_word))
        print(f"You make {game_state.mistakes} mistakes!")
        print()


def play_game():
    answer = input('Do you wanna play Hangman : "Yes" or "No" : ').lower()
    if answer.startswith('y'):
        game_state = HangmanGameState()
        while not is_game_finished(game_state):
            letter = get_user_input(game_state)
            handle_user_input(game_state, letter)
        if game_state.mistakes > 10:
            print(f'you loose my word was: {game_state.secret_word}')
        else:
            print(f'You win my word was: {game_state.secret_word}')
    elif answer.startswith('n'):
        print('Ok Good lack!')
        sys.exit()
    else:
        print('Wrong choice. Good bye!')
        sys.exit()


if __name__ == '__main__':
    play_game()
