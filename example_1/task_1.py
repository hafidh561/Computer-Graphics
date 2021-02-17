from Line import Line


def main():
    # Choose Examples

    coordinatesA = ((-5, 5), (1, 2))
    line = Line(coordinatesA[0], coordinatesA[1])
    line.draw_line_normal()

    # coordinatesB = ((4, 3), (8, -2))
    # line = Line(coordinatesB[0], coordinatesB[1])
    # line.draw_line_normal()

    # coordinatesC = ((2, 3), (5, 3))
    # line = Line(coordinatesC[0], coordinatesC[1])
    # line.draw_line_normal()

    # coordinatesD = ((2, 3), (2, 5))
    # line = Line(coordinatesD[0], coordinatesD[1])
    # line.draw_line_normal()

    # coordinatesE = ((6, 4), (2, 1))
    # line = Line(coordinatesE[0], coordinatesE[1])
    # line.draw_line_normal()


if __name__ == '__main__':
    main()
