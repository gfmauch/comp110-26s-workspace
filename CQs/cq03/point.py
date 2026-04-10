from __future__ import annotations
class Point:
    """2D graph"""
    x: float
    y: float
    def __init__(self, x_init: float, y_init: float) -> None:
        """Initializes point of x and y"""
        self.x = x_init
        self.y = y_init
    def scale_by(self, factor: int) -> None:
        """Mutates a point, updates x and y"""
        self.x = self.x * factor
        self.y = self.y * factor
    def scale(self, factor: int) -> Point:
        """Creates not points, does not mutate"""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        return Point(new_x, new_y)