import random
import telebot
import configure

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
        self.is_game_started = False


bot = telebot.TeleBot(configure.config['token'])
game_state = HangmanGameState()


def is_valid_letter(user_input: str) -> bool:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return len(user_input) == 1 and user_input in alphabet


@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, "Howdy, do you want start play Hangman? 'yes'/'no'")


@bot.message_handler(content_types=["text"])
def user_input_handler(message):
    #  TODO: 1 Come up with a way to get rid of global variable game_state
    #  TODO: 2 Split the code below into several functions to increase readability
    global game_state
    user_input = message.text.lower()
    if user_input == 'yes':
        game_state.is_game_started = True
        bot.send_message(message.chat.id, "Ok let's do it. Enter your letter!")
        return
    if not game_state.is_game_started and user_input == 'no':
        bot.send_message(message.chat.id,
                         "I understand you're a busy person, take a brake and play the game! 'yes'/'no'")
    if game_state.is_game_started:
        if not is_valid_letter(user_input):
            bot.reply_to(message, 'Expecting a single Russian letter. Try again.')
            return
        else:
            if user_input not in game_state.letters:
                game_state.letters.append(user_input)
            else:
                bot.reply_to(message, 'This letter has already been entered. Try again')
                return
            if user_input in game_state.secret_word:
                for ind, value in enumerate(game_state.secret_word):
                    if value == user_input:
                        game_state.visual_word[ind] = user_input
            else:
                game_state.mistakes += 1
                bot.send_message(message.chat.id, f"Wrong guess! You made {game_state.mistakes} mistakes!")
            bot.send_message(message.chat.id, "My word is :" + ''.join(game_state.visual_word))
            if is_game_finished(game_state):
                if game_state.mistakes >= 10:
                    bot.send_message(message.chat.id, f'You loose, my word was: {game_state.secret_word}')
                else:
                    bot.send_message(message.chat.id, f'You win, my word was: {game_state.secret_word}')
                game_state = HangmanGameState()
                bot.send_message(message.chat.id, "Do you want to play again? 'yes'/'no'")


def is_game_finished(game_state: 'HangmanGameState') -> bool:
    return '_' not in game_state.visual_word or game_state.mistakes >= 10


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
