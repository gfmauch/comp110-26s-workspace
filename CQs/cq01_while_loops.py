"""cq01_while_loops.py"""
__author__="730822602"

def num_instances(phrase: str, search_char: str) -> int:
    """While loop to count the number of characters in the index"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count

def get_evens(numbers: str) -> str:
    """While loop to find the number of even numbers"""
    evens: str = ""
    index: int = 0
    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            evens = evens + numbers[index]
        index = index + 1
    return evens