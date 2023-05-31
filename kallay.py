# https://www.personal.kent.edu/~rmuhamma/Compgeometry/MyCG/ConvexHull/incrementCH.htm
from utils import create_points

points = create_points(8)

def position(a, b, c):
     # Takes the line formed by a and b and check if c is in one side or another
     return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) > 0

def is_tangency(CH, point):
    # Take CH already sorted by x values
    if (position(point, CH[-1], CH[-2]) and position(point, CH[-2], CH[-3])):
        return True
    return False


def kallay(points):
    # Step 1: Sort points by x values
    S = sorted(points, key=lambda tup: tup[0])

    # Step 2: Select initial triangle
    CH = S[:3]

    # Step 3: Iterate through remaining points
    for i in range(len(S)):
        # Finde upper tangency point
        u = CH[-1]

        # Find lower tangency point
    return 0

kallay(points=points)

