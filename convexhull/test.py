from random import seed

from graham import graham
from jarvis import jarvis
from exhaustive import exhaustive
from shamos import shamos
from utils import create_points, scatter_plot


def main():
    seed(0)
    pts = create_points(6)
    scatter_plot(pts, [[]], title="convex hull : initial set", show=True, save=False)
    print("Points:", pts)
    hull = exhaustive(pts, True, show=True, save=False)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=True, save=False)


if __name__ == "__main__":
    main()
