import numpy as np
from Geometry.vector_2D import Vector2D

class PointSetGenerator:
  """
  Class for generating random sets of 2D points. The class provides a method for generating a set of
  random points in 2D space.
  """

  def random_points(self, n: int) -> np.ndarray[Vector2D]:
    """ Generates a set of random 2D points. """
    points: np.ndarray[Vector2D] = []
    for i in range(n):
      random_point = Vector2D(np.random.uniform(), np.random.uniform())
      points.append(random_point)

    return np.array(points) 
