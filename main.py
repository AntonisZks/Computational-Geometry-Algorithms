from Geometry.convex_hull import Convex_Hull
from Algorithms.graham_scan import GrahamScanAlgorithm
from tools.point_set_generator import PointSetGenerator as SetGen

if __name__ == "__main__":
  # Create a generator object and generate a set of random points
  generator = SetGen()
  points = generator.random_points(100)

  # Create a Graham Scan algorithm object and compute the convex hull
  gs_algorithm = GrahamScanAlgorithm()
  gs_result = gs_algorithm(points)
  hull = Convex_Hull(points, gs_result)

  # Plot the convex hull
  hull.plot()
