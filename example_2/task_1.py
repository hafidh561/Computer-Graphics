from Circle import Circle
import  sys

def main():
    sys.setrecursionlimit(2925)
    center = (0, 0)
    radius = 6
    example_2 = Circle(center, radius)
    example_2.run()

    # center = (2, 5)
    # radius = 6
    # example_2 = Circle(center, radius)
    # example_2.run()


if __name__ == "__main__":
    main()