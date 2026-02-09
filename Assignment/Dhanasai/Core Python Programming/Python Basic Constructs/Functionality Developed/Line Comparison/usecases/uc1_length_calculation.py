from model.point import Point
from model.line import Line

def main():
    point1 = Point(1, 2)
    point2 = Point(4, 6)

    line = Line(point1, point2)
    print("Length of the line:", line.length())

if __name__ == "__main__":
    main()
