"""Mutating Functions"""
__author__= "730822602"

def manual_append(first_list: list[int], input_var: int) -> None:
    """mutates input through appending"""
    list.append(first_list, input_var)

def double(second_list: list[int]) -> None:
    """Mutates the input by multiplying by 2"""
    index: int = 0
    while index < len(second_list):
        second_list[index] *= 2
        index += 1

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)

print(list_1)
print(list_2)