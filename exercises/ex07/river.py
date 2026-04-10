"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730822602"

class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Implement the inevitable death of all of god's creatures if they are too old."""
        for curFish in reversed(self.fish):
            if (curFish.age > 3):
                self.fish.remove(curFish)
        
        for curBear in reversed(self.bears):
            if (curBear.age > 5):
                self.bears.remove(curBear)

        return None

    def bears_eating(self):
        for curBear in self.bears:
            if (len(self.fish) >= 5):
                curBear.eat(3)
                self.remove_fish(3)
                
        return None

    def check_hunger(self):
        for curBear in reversed(self.bears):
            if (curBear.hunger_score < 0):
                self.bears.remove(curBear)
        
        return None

    def repopulate_fish(self):
        """Repopulate fish."""
        numOffspring : int = int(len(self.fish) / 2) * 4
        for _ in range(0, numOffspring):
            self.fish.append(Fish())
    
        return None

    def repopulate_bears(self):
        """Repopulate bears."""
        numBears : int = len(self.bears)
        numOffspring : int = int(numBears / 2)
        for _ in range(0, numOffspring):
            self.bears.append(Bear())

        return None
    
    def remove_fish(self, amount:int):
        for _ in range(0, amount):
            self.fish.pop(0)

        return None

    def __str__(self) -> str:
        """Visual representation of the River state."""
        return f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}"
    
    def __add__(self, other_riv: River) -> River:
        """Create a new river with self + other_riv number of creatures."""
        numBears : int = len(self.bears) + len(other_riv.bears)
        numFish : int = len(self.fish) + len(other_riv.fish)
        return River(numFish, numBears)
    
    def __mul__(self, factor: int) -> River:
        """Create a river that is 'factor' bigger than this river."""
        numBears : int = len(self.bears) * factor
        numFish : int = len(self.fish) * factor
        return River(numFish, numBears)

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """Simulate the elapsig of one calendar week in the river."""
        for _ in range (0, 7):
            self.one_river_day()