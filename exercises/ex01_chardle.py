"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730658668"

user_input_word: str = input("Enter a 5-character word: ")

if len(user_input_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

user_input_character: str = input("Enter a single character: ")

if len(user_input_character) != 1:
    print("Error: Character must be a single character.")
    exit()

total_index_instances: int = 0

print("Searching for " + user_input_character + " in " + user_input_word)

if user_input_word[0] == user_input_character: 
    print(user_input_character + " found at index 0")
    total_index_instances += 1
if user_input_word[1] == user_input_character:
    print(user_input_character + " found at index 1")
    total_index_instances += 1
if user_input_word[2] == user_input_character:
    print(user_input_character + " found at index 2")
    total_index_instances += 1
if user_input_word[3] == user_input_character:
    print(user_input_character + " found at index 3")
    total_index_instances += 1
if user_input_word[4] == user_input_character:
    print(user_input_character + " found at index 4")
    total_index_instances += 1

if total_index_instances == 0: 
    print("No instances of " + user_input_character + " found in " + user_input_word)
elif total_index_instances == 1: 
    print(str(total_index_instances) + " instance of " + user_input_character + " found in " + user_input_word)
else: 
    print(str(total_index_instances) + " instances of " + user_input_character + " found in " + user_input_word)