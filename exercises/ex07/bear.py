"""File to define Bear class."""

class Bear:
    def __init__(self):
        """Initilizes age and hunger."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increment age."""
        self.age = self.age + 1
        self.hunger_score = self.hunger_score - 1;

    def eat(self, num_fish : int):
        """When a bear eats."""
        self.hunger_score += num_fish;