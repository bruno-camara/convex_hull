from random import seed

from graham import graham
from jarvis import jarvis
from exhaustive import exhaustive
from shamos import shamos
from utils import create_points, scatter_plot


def main():
    seed(0)
    pts = create_points(100)
    scatter_plot(pts, [[]])
    print("Points:", pts)
    hull = exhaustive(pts, True)
    print("Hull:", hull)
    scatter_plot(pts, [hull])


if __name__ == "__main__":
    main()
