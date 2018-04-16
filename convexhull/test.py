from naive import naive
from utils import create_points, scatter_plot


def main():
    pts = create_points(5)
    scatter_plot(pts, [[]])
    print("Points:", pts)
    hull = naive(pts, True)
    print("Hull:", hull)
    scatter_plot(pts, [hull])


if __name__ == "__main__":
    main()
