from math import atan2  # for computing polar angle
from random import randint  # for sorting and creating data pts

from matplotlib import pyplot as plt  # for plotting


# Returns a list of (x,y) coordinates of length 'num_points',
# each x and y coordinate is chosen randomly from the range
# 'min' up to 'max'.
def create_points(ct, minimum=0, maximum=50):
    return [[randint(minimum, maximum), randint(minimum, maximum)] for _ in range(ct)]


# Creates a scatter plot, input is a list of (x,y) coordinates.
# The second input 'convex_hull' is another list of (x,y) coordinates
# consisting of those points in 'coords' which make up the convex hull,
# if not None, the elements of this list will be used to draw the outer
# boundary (the convex hull surrounding the data points).
def scatter_plot(coords, convex_hulls=None):
    xs, ys = zip(*coords)  # unzip into x and y coord lists
    plt.scatter(xs, ys)  # plot the data points

    if convex_hulls is not None:
        for convex_hull in convex_hulls:
            # plot the convex hull boundary, extra iteration at
            # the end so that the bounding line wraps around
            for i in range(1, len(convex_hull) + 1):
                if i == len(convex_hull):
                    i = 0  # wrap
                c0 = convex_hull[i - 1]
                c1 = convex_hull[i]
                plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'r')
    plt.show()


# Determines whether a (x,y) point in inside a polygon defined as a list of (x,y) points.
def point_in_polygon(point, poly):
    x = point[0]
    y = point[1]
    n = len(poly)
    inside = False
    xints = 0.0
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


# Returns the polar angle (radians) from p0 to p1.
# If p1 is None, defaults to replacing it with the
# global variable 'anchor', normally set in the
# 'graham_scan' function.
def polar_angle(p0, p1):
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return atan2(y_span, x_span)


# Returns the euclidean distance from p0 to p1,
# square root is not applied for sake of speed.
# If p1 is None, defaults to replacing it with the
# global variable 'anchor', normally set in the
# 'graham_scan' function.
def distance(p0, p1):
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return y_span ** 2 + x_span ** 2


# Returns the determinant of the 3x3 matrix...
#  [p1(x) p1(y) 1]
#  [p2(x) p2(y) 1]
#  [p3(x) p3(y) 1]
# If >0 then counter-clockwise
# If <0 then clockwise
# If =0 then collinear
def det(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) \
           - (p2[1] - p1[1]) * (p3[0] - p1[0])


# Determines whether a set of points constitutes a convex polygon.
def is_convex(points):
    i = 0
    while det(points[i % len(points)], points[(i + 1) % len(points)], points[(i + 2) % len(points)]) <= 0 and i < len(
            points):
        i = i + 1
    return i == len(points)


# Sorts in order of increasing polar angle from 'anchor' point.
# 'anchor' variable is assumed to be global, set from within 'graham_scan'.
# For any values with equal polar angles, a second sort is applied to
# ensure increasing distance from the 'anchor' point.
def quicksort(a, anchor):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    piv_ang = polar_angle(a[randint(0, len(a) - 1)], anchor)  # select random pivot
    for pt in a:
        pt_ang = polar_angle(pt, anchor)  # calculate current point angle
        if pt_ang < piv_ang:
            smaller.append(pt)
        elif pt_ang == piv_ang:
            equal.append(pt)
        else:
            larger.append(pt)
    return quicksort(smaller, anchor) + sorted(equal, key=lambda x: distance(x, anchor)) + quicksort(larger, anchor)
