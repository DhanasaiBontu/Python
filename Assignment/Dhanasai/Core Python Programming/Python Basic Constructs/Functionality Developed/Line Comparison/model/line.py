from math import sqrt
from model.point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start = start_point
        self.end = end_point

    def length(self) -> float:
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        return sqrt(dx ** 2 + dy ** 2)

    def equals(self, other_line) -> bool:
        return (self.start.x == other_line.start.x and
                self.start.y == other_line.start.y and
                self.end.x == other_line.end.x and
                self.end.y == other_line.end.y)

    def compare_to(self, other_line) -> int:
        if self.length() == other_line.length():
            return 0
        elif self.length() > other_line.length():
            return 1
        else:
            return -1
