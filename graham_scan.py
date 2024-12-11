import numpy as np
from vector_2D import Vector2D
from abc import ABC, abstractmethod


class ConvexHullSolutionAlgorithm(ABC):

  @abstractmethod
  def __call__(self, points: np.ndarray[Vector2D]) -> np.ndarray[Vector2D]:
    pass


class GrahamScanAlgorithm(ConvexHullSolutionAlgorithm):

  def __is_right_turn(self, p1: Vector2D, p2: Vector2D, p3: Vector2D) -> bool:
    # Define the supporting matrix for the three points to determine the orientation of the points
    matrix: np.ndarray[np.ndarray[float]] = np.array([
      [1, p1.x, p1.y], 
      [1, p2.x, p2.y], 
      [1, p3.x, p3.y]
    ])
    return np.linalg.det(matrix) < 0
  
  def __construct_upper_hull(self, points: np.ndarray[Vector2D]) -> np.ndarray[Vector2D]:
    L_upper: np.ndarray[Vector2D] = [points[0], points[1]]

    # Construct the upper hull of the convex hull
    for i in range(2, len(points)):
      L_upper.append(points[i])
      while len(L_upper) > 2 and not self.__is_right_turn(L_upper[-3], L_upper[-2], L_upper[-1]):
        L_upper.pop(-2)

    return L_upper
  
  def __construct_lower_hull(self, points: np.ndarray[Vector2D]) -> np.ndarray[Vector2D]:
    L_lower: np.ndarray[Vector2D] = [points[-1], points[-2]]

    # Construct the lower hull of the convex hull
    for i in range(len(points) - 3, -1, -1):
      L_lower.append(points[i])
      while len(L_lower) > 2 and not self.__is_right_turn(L_lower[-3], L_lower[-2], L_lower[-1]):
        L_lower.pop(-2)

    # Remove the first and last points from L_lower to avoid duplication
    L_lower.pop(0)
    L_lower.pop(-1)

    return L_lower

  def __call__(self, points: np.ndarray[Vector2D]) -> np.ndarray[Vector2D]:
    # Sort the points by their x-coordinate, then by their y-coordinate, and insert p1 and p2 to the L_upper set
    points: np.ndarray[Vector2D] = sorted(points, key=lambda p: (p.x, p.y))
    
    # Construct the upper and lower hulls of the convex hull
    L_upper: np.ndarray[Vector2D] = self.__construct_upper_hull(points)
    L_lower: np.ndarray[Vector2D] = self.__construct_lower_hull(points)

    # Merge the L_upper and L_lower sets to form the convex hull and return the result
    L: np.ndarray[Vector2D] = L_upper + L_lower

    return L
