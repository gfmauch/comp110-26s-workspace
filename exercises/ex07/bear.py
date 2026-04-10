"""File to define Bear class."""

class Bear:
    def __init__(self):
        """Initilizes age and hunger."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increment age."""
        self.age = self.age + 1