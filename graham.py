# https://www.geeksforgeeks.org/convex-hull-using-graham-scan/
from utils import create_points, polar_angle, distance, polar_quicksort, is_convex

def remove_duplicates(lst):
    # Create an empty dictionary to store tuples as keys
    encountered = {}
    # Create an empty list to store unique tuples
    result = []
    # Iterate through the input list
    for tup in lst:
        # If the tuple has not been encountered before,
        # add it to the dictionary and the result list
        if tup not in encountered:
            encountered[tup] = True
            result.append(tup)
    # Return the list of unique tuples
    return result

points = create_points(8)

print(points)

def graham(points):
    # Step 1: Find P, the bottom-most point
    p0 = min(points, key = lambda t: t[1])

    # Step 2: Transform the points to polar coordinates
    points_polar = []
    for i in points:
        points_polar.append([distance(p0, i), polar_angle(p0, i)])
    
    # Step 3: Sort by the polar angle
    #points_polar_sorted = sorted(points_polar, key=lambda t: (t[1], t[0]))
    points_sorted = polar_quicksort(points, p0)
    print(p0)
    print(points_polar)
    
    print(points_sorted)

    # Step 4: Remove points with same angle
    print('Probabilidade baixa')

    # Step 5
    S = points_sorted[:3] #Create an empty stack ‘S’ and push points[0], points[1] and points[2] to S.
    for point in points_sorted[3:]:
        S.append(point)
        if not is_convex(S):
            print("Concave - Remove last point")
            next = S.pop()
            S.pop()
            S.append(next)
    
    return S

print(graham(points=points))
