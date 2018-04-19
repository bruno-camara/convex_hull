from random import seed

from exhaustive import exhaustive
from utils import create_points, scatter_plot, is_convex


def main():
    seed(0)
    pts = create_points(8)
    show = True  # to display a frame
    save = False  # to save into .png files in "figs" directory
    scatter_plot(pts, [[]], title="convex hull : initial set", show=show, save=save)
    print("Points:", pts)
    hull = exhaustive(pts, show=show, save=save)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=True, save=save)


if __name__ == "__main__":
    main()
