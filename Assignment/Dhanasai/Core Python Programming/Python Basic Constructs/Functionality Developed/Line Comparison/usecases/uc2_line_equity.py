from model.point import Point
from model.line import Line

def main():
    line1 = Line(Point(1, 2), Point(4, 6))
    line2 = Line(Point(1, 2), Point(4, 6))
    line3 = Line(Point(0, 0), Point(3, 4))

    print("Line1 equals Line2?", line1.equals(line2))
    print("Line1 equals Line3?", line1.equals(line3))

if __name__ == "__main__":
    main()
