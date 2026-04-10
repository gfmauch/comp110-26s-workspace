"""EXO2 - Chardle - A cute step toward Wordle."""

__author__ = "730822602"

def input_word() -> str:
    """Gathers word from user."""
    word: str = input("Enter a 5-character word: ")

    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()

def input_letter() -> str:
    """Gathers word from user"""
    letter: str = input("Enter a single character: ")

    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()

def contains_char(word: str, letter: str) -> None:
    """Checks to see if letter is in index and states number of instances."""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)

def main() -> None:
    """Putting everything together."""
    contains_char(word=input_word(), letter=input_letter())
if __name__ == "__main__":
    main()