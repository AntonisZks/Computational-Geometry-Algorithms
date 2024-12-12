import numpy as np
from Geometry.vector_2D import Vector2D
from matplotlib import pyplot as plt


class Convex_Hull:
  """
  Class representing the convex hull of a set of points. The convex hull is represented by the points
  that form the hull, as well as the edges that connect the points.
  """

  def __init__(self, points: np.ndarray[Vector2D], hull_points: np.ndarray[Vector2D]):
    self.points = points
    self.hull_points = hull_points
    self.edges = self.__construct_edges(hull_points)

  def __construct_edges(self, hull_points: np.ndarray[Vector2D]):
    """ Constructs the edges list of the convex hull. """
    edges = []

    for i in range(len(hull_points) - 1):
        edges.append((hull_points[i], hull_points[i + 1]))
    edges.append((hull_points[-1], hull_points[0]))

    return edges

  def __repr__(self):
    return f"Convex_Hull\n-points={self.points}\n-edges={self.edges}"
  
  def plot(self, axes: plt.axes = None, title: str = ""):
    """ Plots the convex hull. This function will plot the points and edges of the convex hull. """
    if axes is not None:
      axes.scatter([point.x for point in self.points], [point.y for point in self.points], color='#339AFF', s=10)

      # Plot the edges of the convex hull
      for edge in self.edges:
        axes.plot([edge[0].x, edge[1].x], [edge[0].y, edge[1].y], color='#FF7070')

      axes.axis('off')
      axes.set_title(title)
    else:
      plt.scatter([point.x for point in self.points], [point.y for point in self.points], color='#339AFF', s=10)

      # Plot the edges of the convex hull
      for edge in self.edges:
        plt.plot([edge[0].x, edge[1].x], [edge[0].y, edge[1].y], color='#FF7070')

      plt.axis('off')
      plt.title(title)
      plt.show()