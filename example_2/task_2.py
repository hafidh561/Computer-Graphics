from Polygon import Polygon


def main():
    vertices1 = [(2, 1), (3, 6), (5, 4), (8, 8), (10, 4), (12, 2), (2, 1)]
    example_1 = Polygon(vertices1)
    example_1.run_scan_line()

    # vertices2 = [(2, 2), (3, 6), (5, 4), (8, 8), (10, 4), (12, 2), (2, 1)]
    # example_2 = Polygon(vertices2)
    # example_2.run_boundary_fill()


if __name__ == "__main__":
    main()
