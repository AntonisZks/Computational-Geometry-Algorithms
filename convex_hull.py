import numpy as np
from vector_2D import Vector2D
from matplotlib import pyplot as plt


class Convex_Hull:
  def __init__(self, points: np.ndarray[Vector2D], edges: list[tuple[Vector2D, Vector2D]]):
    self.points = points
    self.edges = edges

  def __repr__(self):
    return f"Convex_Hull\n-points={self.points}\n-edges={self.edges}"
  
  def plot(self, plot_edges: bool = True):
    """
    Plot the convex hull. This function will plot the points and edges of the convex hull.
    """
    plt.figure()
    plt.scatter([point.x for point in self.points], [point.y for point in self.points], color='#339AFF', s=10)

    # Plot the edges of the convex hull if asked
    if plot_edges:
      for edge in self.edges:
        plt.plot([edge[0].x, edge[1].x], [edge[0].y, edge[1].y], color='#FF7070')

    plt.axis('off')
    plt.show()
