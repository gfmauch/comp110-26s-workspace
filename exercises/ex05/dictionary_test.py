from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
"""checks dictionary with unit tests."""
author = "730822602"


def test_letters() -> None:
    """Test the invert function with different letters."""
    assert invert({'f': 'j', 'd': 'k'}) == ({'j': 'f', 'k': 'd'})


def test_words() -> None:
    """Test the invert function with different words."""
    assert invert({'italian': 'pasta', 'japanese': 'soba'})


def test_empty() -> None:
    """Test invert function to return empty dictionary."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {}


def test_color_favorite() -> None:
    """Test to count favorite color."""
    color = {"Andrew": "Violet", "Greg": "Red", "Kate": "Violet"}
    assert favorite_color(color) == "Violet"


def test_tie() -> None:
    """Test output when there is a tie - return first color."""
    color = {"Graham": "Purple", "Parker": "Green"}
    assert favorite_color(color) == "Purple"


def test_multi_tie() -> None:
    """Test output for large tie."""
    color = {"Graham": "Violet", "Greg": "Green", "Parker": "Green", "Andrew": "Violet"}
    assert favorite_color(color) == "Green"  # green would be the output, it got to 2 first


def test_count_input() -> None:
    """State each input and the number of inputs correctly."""
    item = ["20", "15", "13", "18"]
    assert count(item) == {20: 1, 15: 1, 13: 1, 18: 1}


def test_different_counts() -> None:
    """States correct number of input."""
    item = ["4", "2", "2", "4"]
    assert count(item) == {"4": 2, "2": 2}


def test_empty_count() -> None:
    """Test counting empty list."""
    assert count([]) == {}


def test_different_letters() -> None:
    """Test alphabet ordering."""
    word = ["pumpernickel", "buffer", "table"]
    assert alphabetizer(word) == {"b": ["buffer"], "p": ["pumpernickel"], "t": ["table"]}


def test_case() -> None:
    """Test alphabetizer for case sensitivity."""
    word = ["Buffer", "buffer"]
    assert alphabetizer(word) == {"b": ["Buffer", "buffer"]}


def test_single_letter() -> None:
    """Test when letter instead of word."""
    word = ["b", "j"]
    assert alphabetizer(word) == {"b": ["b"], "j": ["j"]}


def test_update_new_day() -> None:
    """Test adding attendance for new day."""
    attendance: dict[str, list[str]] = {"Monday": ["Graham"]}
    update_attendance(attendance, "Tuesday", "Greg")
    assert attendance == {"Monday": ["Graham"], "Tuesday": ["Greg"]}


def test_update_new_student() -> None:
    """Test adding a new student to a day."""
    attendance: dict[str, list[str]] = {"Monday": ["Graham"]}
    update_attendance(attendance, "Monday", "Greg")
    assert attendance == {"Monday": ["Graham", "Greg"]}


def test_duplicate_student() -> None:
    """Student shouldn't be added twice."""
    attendance: dict[str, list[str]] = {"Monday": ["Graham"]}
    update_attendance(attendance, "Monday", "Graham")
    assert attendance == {"Monday": ["Graham"]}