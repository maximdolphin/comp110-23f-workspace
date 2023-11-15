"""EX02 - One Shot Wordle - Creating a one-shot wordle using loops!"""

__author__ = "730658668"

secret_word: str = "python"
secret_word_length: int = len(secret_word)
guess_word: str = input(f"What is your {secret_word_length}-letter guess?")
guess_word_index: int = 0
emoji_string: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess_word) != secret_word_length:
    guess_word = input(f"That was not {secret_word_length} letters! Try again:")

if len(guess_word) == secret_word_length:
    while guess_word_index < secret_word_length:
        if guess_word[guess_word_index] == secret_word[guess_word_index]:
            emoji_string += GREEN_BOX
        else:
            character_in_word: bool = False
            guess_alternate_index: int = 0

            while not character_in_word and guess_alternate_index < secret_word_length:
                if guess_word[guess_word_index] == secret_word[guess_alternate_index]:
                    character_in_word = True
                else:
                    guess_alternate_index += 1

            if character_in_word:
                emoji_string += YELLOW_BOX
            else:
                emoji_string += WHITE_BOX

        guess_word_index += 1

if guess_word == secret_word:
    print(emoji_string)
    print("Woo! You got it!")
else:
    print(emoji_string)
    print("Not quite. Play again soon!")
