import math
import sys
import time
import os
from math import atan2  # for computing polar angle
from random import randint, sample  # for sorting and creating data pts

from matplotlib import pyplot as plt  # for plotting


# Returns a list of unique (x,y) coordinates of length 'num_points',
# each x and y coordinate is chosen randomly from the range
# 'min' up to 'max'.
def create_points(ct, minimum=0, maximum=50):
    delta = maximum - minimum
    if delta * delta < ct:
        raise ValueError("Number of points too large for the available space")
    ps = sample(range(0, delta * delta), ct)
    points = []
    for p in ps:
        points.append([(p % delta) + minimum, (p // delta) + minimum])
    return points


# Creates a scatter plot, input is a list of (x,y) coordinates.
# The second input 'convex_hull' is another list of (x,y) coordinates
# consisting of those points in 'coords' which make up the convex hull,
# if not None, the elements of this list will be used to draw the outer
# boundary (the convex hull surrounding the data points).
def scatter_plot(coords, convex_hulls=None, all_points=[], minimum=0, maximum=50, title="convex hull",
                 show=False, save=True):
    fig = plt.figure(title)
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_xlim(xmin=minimum, xmax=maximum)
    ax.set_ylim(ymin=minimum, ymax=maximum)

    if len(all_points) > 0:
        xall, yall = zip(*all_points)  # unzip into x and y coord lists
        plt.scatter(xall, yall, c='gray')  # plot the data points
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
    if show:
        plt.show()
    if save:
        directory = "./figs/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = directory + "convexhull_" + repr(time.time()) + ".png"
        fig.savefig(file, bbox_inches='tight')


# Determines whether a (x,y) point in inside a convex polygon defined as a list of (x,y) points.
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
def determinant(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) \
           - (p2[1] - p1[1]) * (p3[0] - p1[0])


# Returns the angle formed by the three points in radians.
def angle(p1, p2, p3):
    return math.acos(
        (distance(p2, p1) + distance(p2, p3) - distance(p1, p3)) / (
                2 * math.sqrt(distance(p2, p1)) * math.sqrt(distance(p2, p3))))


# Determines whether a set of points constitutes a convex polygon.
def is_convex(points):
    if len(points) == 3:
        return True
    same_sign = True
    turn = angle(points[0], points[1], points[2])
    total = 180 - math.degrees(turn)
    i = 1
    while same_sign and i < len(points):
        new_turn = angle(points[(i + 0) % len(points)], points[(i + 1) % len(points)], points[(i + 2) % len(points)])
        total = 180 - math.degrees(new_turn) + total
        i = i + 1
        same_sign = (new_turn * turn) >= 0
        turn = new_turn
    return i == len(points) and (total % 360) <= (math.degrees(2 * math.pi) % 360)


# Sorts in order of increasing polar angle from 'anchor' point.
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
