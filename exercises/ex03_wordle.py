"""Wordle"""
__author__ = "730822602"

def input_guess(secret_word_len: int) -> str:
    """Correct length or error while loops"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    # While loop to make sure the word is the proper length
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess

def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks index for character, if found states how many times it was found."""
    assert len(char_guess) ==  1
    index: int = 0
    # While loop to check if a character is in the word (true or false)
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False

def emojified(guess: str, secret_word: str) -> str:
    """Accuracy of a guess is represented by the color of boxes"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji_result: str = ""
    # While loop to check every letter in the index/provided word and put in the
    # correct color box until the end of the index
    while index < len(guess):
        if guess[index] == secret_word[index]:
            emoji_result += GREEN_BOX
        elif contains_char(secret_word, guess[index]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        index += 1
    return emoji_result

def main(secret_word: str) -> None:
    """the entry point of the program and main game loop."""
    turns: int = 1
    max_turns: int = 6
    won: bool = False
    # While loop to print the correct things for each turn and 
    # allow for new guesses the defined number of times
    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        
        if guess == secret_word:
            won = True
        else:
            turns += 1
    
    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret_word="codes")