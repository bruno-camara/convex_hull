from random import seed

from graham import graham
from jarvis import jarvis
from exhaustive import exhaustive
from shamos import shamos
from utils import create_points, scatter_plot


def main():
    seed(0)
    pts = create_points(100)
    scatter_plot(pts, [[]], title="convex hull : initial set", show=False, save=True)
    print("Points:", pts)
    hull = exhaustive(pts, True)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=False, save=True)


if __name__ == "__main__":
    main()
