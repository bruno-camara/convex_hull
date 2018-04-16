from random import seed
from time import time

from graham import graham
from jarvis import jarvis
from naive import naive
from shamos import shamos
from utils import *


# For each size in the 'sizes' list, compute the average
# time to find the Convex Hull for a dataset of that size,
# the range used for max and min for the create_points function
# is always 10 times the highest value in the 'sizes' list.
def benchmark(sizes=(1, 10, 100, 1000, 10000), method=graham):
    print(method)
    for s in sizes:
        tot = 0.0
        for _ in range(3):
            points = create_points(s, 0, max(sizes) * 10)
            t0 = time()
            method(points, False)
            tot += (time() - t0)
        print("size %d time: %0.5f" % (s, tot / 3.0))


seed(0)
algorithms = [naive, graham, jarvis, shamos]

for algorithm in algorithms:
    benchmark([2, 4, 6, 8, 10], method=algorithm)
