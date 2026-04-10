class Fish:
    age: int
    def __init__(self):
        """Initilizes age."""
        self.age = 0
        return None

    def one_day(self):
        """Increment age."""
        self.age = self.age + 1;
        return None