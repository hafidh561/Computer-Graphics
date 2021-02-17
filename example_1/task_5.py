from Circle import Circle


def main():
    center = (4, 4)
    radius = 2

    example_1 = Circle(center, radius)
    example_1.draw_circle_bresenham()


if __name__ == '__main__':
    main()
