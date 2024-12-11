from vector_2D import Vector2D
from graham_scan import GrahamScanAlgorithm
import numpy as np
from convex_hull import Convex_Hull


if __name__ == "__main__":
  # Generate a circular set of random 100 2D points
  points: np.ndarray[Vector2D] = []
  for i in range(1000):
    angle = np.random.uniform(0, 2 * np.pi)
    radius = np.random.uniform(0, 1)
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    points.append(Vector2D(x, y))

  algorithm = GrahamScanAlgorithm()

  convex_hull_points: np.ndarray[Vector2D] = algorithm(points)
  convex_hull_edges = []
  for i in range(len(convex_hull_points) - 1):
    convex_hull_edges.append((convex_hull_points[i], convex_hull_points[i + 1]))
  convex_hull_edges.append((convex_hull_points[-1], convex_hull_points[0]))

  convex_hull = Convex_Hull(points, convex_hull_edges)
  convex_hull.plot()
