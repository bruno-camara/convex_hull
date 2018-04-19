from random import seed

from graham import graham
from jarvis import jarvis
from exhaustive import exhaustive
from shamos import shamos
from utils import create_points, scatter_plot


def main():
    seed(0)
    pts = create_points(8)
    show = True
    save = False
    scatter_plot(pts, [[]], title="convex hull : initial set", show=show, save=save)
    print("Points:", pts)
    hull = exhaustive(pts, True, show=show, save=save)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=show, save=save)


if __name__ == "__main__":
    main()
