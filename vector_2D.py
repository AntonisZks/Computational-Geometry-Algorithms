import numpy as np


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x:.3f}, {self.y:.3f})"
