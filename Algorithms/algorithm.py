from abc import ABC, abstractmethod
from Geometry.vector_2D import Vector2D
import numpy as np


class ConvexHullSolutionAlgorithm(ABC):
  """
  Abstract class for convex hull solution algorithms. All algorithms that implement this class,
  must implement the __call__ method, which executes their individual solution process. Users cannot
  instantiate this class directly, but must use one of its subclasses.
  """

  @abstractmethod
  def __call__(self, points: np.ndarray[Vector2D]) -> np.ndarray[Vector2D]:
    """
    Abstract method that must be implemented by all algorithms that inherit from this class.
    This method should execute the algorithm's solution process and return the convex hull of the
    input points.
    """
    ...
