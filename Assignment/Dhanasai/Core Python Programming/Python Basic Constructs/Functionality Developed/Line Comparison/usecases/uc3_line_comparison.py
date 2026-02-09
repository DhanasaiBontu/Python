from model.point import Point
from model.line import Line

def main():
    line1 = Line(Point(1, 2), Point(4, 6))
    line2 = Line(Point(0, 0), Point(3, 4))

    comparison = line1.compare_to(line2)
    if comparison == 0:
        print("Lines are equal in length.")
    elif comparison > 0:
        print("Line1 is longer than Line2.")
    else:
        print("Line1 is shorter than Line2.")

if __name__ == "__main__":
    main()
