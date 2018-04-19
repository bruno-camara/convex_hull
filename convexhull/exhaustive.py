# Returns the vertices comprising the boundaries of
# convex hull containing all points in the input set.
# The input 'points' is a list of (x,y) coordinates.
# If 'show_progress' is set to True, the progress in
# constructing the hull will be plotted on each iteration.
# Uses a very naive method: iterates over the whole set of convex polygons for size 3 to n

from itertools import permutations

from utils import is_convex, scatter_plot, point_in_polygon


def exhaustive(points, show_progress=False, show=True, save=False):
    i = 3
    while i <= len(points):
        for subset in permutations(points, i):
            if is_convex(subset):
                if show_progress:
                    scatter_plot(points, [subset], title="exhaustive search", show=show, save=save)
                one_out = False
                j = 0
                while not one_out and j < len(points):
                    point = points[j]
                    if point not in list(subset) and not point_in_polygon(point, list(subset)):
                        one_out = True
                    j = j + 1
                if not one_out:
                    return subset
        i = i + 1
    return points
