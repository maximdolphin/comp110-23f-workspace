"""EXO3 - One Shot Wordle - Creating a wordle using functions."""

__author__ = "730658668"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(input_word: str, input_char: str) -> bool:
    """Return True if input_char is found in input_word, False otherwise."""
    assert len(input_char) == 1
    input_word_length = len(input_word)
    guess_index: int = 0
    character_in_word: bool = False
    while not character_in_word and guess_index < input_word_length:
        if input_char == input_word[guess_index]:
            character_in_word = True
        else:
            guess_index += 1
    return character_in_word


def emojified(secret_word: str, guess_word: str) -> str:
    """Return emoji representation based on comparison between secret and guess word."""
    assert len(guess_word) == len(secret_word)
    guess_word_length: int = len(guess_word)
    guess_word_index: int = 0
    emoji_string: str = ""

    while guess_word_index < guess_word_length:
        chr_in_word = contains_char(secret_word, guess_word[guess_word_index])
        if guess_word[guess_word_index] == secret_word[guess_word_index]:
            emoji_string += GREEN_BOX
        elif chr_in_word:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX

        guess_word_index += 1

    return emoji_string


def input_guess(expected_length: int) -> str:
    """Checks to make sure that the guess word is of the expected length."""
    guess_word: str = input(f"Enter a {expected_length} character word:")
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again:")
    return guess_word


def main() -> None:
    """The entrypoint of the program and game loop."""
    game_turn: int = 1
    secret_word: str = "codes"
    game_won: bool = False
    while game_turn <= 6 and not game_won:
        print(f"=== Turn {game_turn}/6 ===")
        guess_word: str = input_guess(len(secret_word))
        if guess_word == secret_word:
            game_won = True
        else:
            print(emojified(secret_word, guess_word))
            game_turn += 1

    if game_turn > 6:
        print("X/6 - Sorry, try again tomorrow!")
    elif game_won:
        print(f"You won in {game_turn}/6 turns!")
        print(emojified(secret_word, guess_word))


if __name__ == "__main__":
    main()