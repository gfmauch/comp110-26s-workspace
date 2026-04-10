"""dictionary in ex05 with invert, favorite color, count, and alphabetization, attendance."""
__author__ = "730822602"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values, keys of input to values of output and values of input become keys of output."""
    inverted_dict: dict[str, str] = {}
    for key in input:  # Value changed to Key
        value = input[key]
        if value in inverted_dict:  # Check if value is a Key input
            raise KeyError("Keys in dictionary must be unique.")
        inverted_dict[value] = key  # Change value to key and key to value
    return inverted_dict


def favorite_color(color_input: dict[str, str]) -> str:
    """Return most frequent color, or color returned first if tie."""
    count: dict[str, int] = {}
    for name in color_input:
        color = color_input[name]
        if color in count:  # increase the count of that color
            count[color] += 1
        else:
            count[color] = 1
    biggest_count: int = 0
    most_frequent: str = ""
    
    for color in count:
        if count[color] > biggest_count:
            biggest_count = count[color]
            most_frequent = color
    return most_frequent


def count(val_list: list[str]) -> dict[str, int]:
    """Count the number of times value is in input list."""
    frequency: dict[str, int] = {}
    for item in val_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Organize words based on the first letter in the word."""
    result: dict[str, list[str]] = {}
    for word in word_list:
        if len(word) > 0 and word[0].isalpha():  # check for alphabetic character start
            first_letter: str = word[0].lower()  # convert first letter to lowercase
            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Take Attendence of students for specific day."""
    if day in attendance:
        if student not in attendance[day]:  # check if student is in list
            attendance[day].append(student)
    else:
        attendance[day] = [student]  # initial creation of attendance list for student
    return None