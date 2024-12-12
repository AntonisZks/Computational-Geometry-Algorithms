import numpy as np


class Vector2D:
    """
    Class representing a 2D vector with x and y coordinates. This class is used to represent points
    in 2D space, and provides methods for performing operations on the vectors.
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        """Outputs the string representation of the vector."""
        return f"({self.x:.3f}, {self.y:.3f})"
