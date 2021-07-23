from random import choice

words = (
    "волдырь", "песок", "лиана", "велосипед", "батискаф", "чернобыль", "повадырь", "лексикон", "амплуа",
    "персонализация",
    "валерьянка", "фантомас", "эверест")

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
selected_word = choice(words)
game_word = ["_"] * len(selected_word)
mistake_counter = 0
user_letters = []
print(''.join(game_word))

while True:
    letter = input("Please input the letter: ").lower()
    if len(letter) != 1:
        print("Sorry please input one letter")
    elif letter not in alphabet:
        print("Sorry please input the Russian letter")
    elif letter not in user_letters:
        user_letters.append(letter)
    elif letter in user_letters:
        print("Sorry you called this letter")
        continue

    if letter in selected_word:
        for i, symbol in enumerate(selected_word):
            if symbol == letter:
                game_word[i] = letter

            if '_' not in game_word:
                print("", "You WIN!!", f"My word was {selected_word}!", sep='\n')
                break
    else:
        mistake_counter += 1
        print(f"You make {mistake_counter} mistake")
        if mistake_counter == 10:
            print("", "LOOSE!!", f"My word was {selected_word}!", sep='\n')
            break

    print(''.join(game_word))
