"""Algorithms to gain familiarity with names and behaviors of commonly used functions."""
__author__= "730822602"

def all (int_list: list[int], indicated_value: int) -> bool:
    """Numbers match indicated number true, """
    if len(int_list) == 0:
        return False
    for value in int_list:  #chck every value in the list
        if value != indicated_value:  #if any value doesnt match, it's false
            return False
    return True

def max(input: list[int]) -> int:
    """Returns the largest num."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_val: int = input[0]
    for val in input:
        if val > max_val:
            max_val = val
    return max_val

def is_equal(equal_1: list[int], equal_2: list[int]) ->bool:
    """Checks if lists are equal"""
    if len(equal_1) != len(equal_2):  #check if the lists are of equal length
        return False
    index: int = 0
    while index < len(equal_1):  # check if the values in the lists match
        if equal_1[index] != equal_2[index]:
            return False
        index += 1
    return True

def extend(first_list: list[int], second_list: list[int]) -> None:
    """Adding the second list to the end of the first list."""
    for val in second_list: 
        first_list.append(val)