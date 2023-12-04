class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # should return: (2.3/43.14)
    def __str__(self):
        return self.print_point()

    # should return: [(2.3/43.14), (5.53/2.5), (12.2/28.7)]
    def __repr__(self):
        return self.print_point()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def print_point(self):
        return f"({self.x}/{self.y})"

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)


class Shape(list[Point, ...]):

    def __init__(self, *points):
        super().__init__(points)

    def __str__(self):
        return f"{[point for point in self]}"

    def __repr__(self):
        return self.__str__()

    # defines behaviour for "=="
    def __eq__(self, other):
        return Shape.centroid(self) == Shape.centroid(other)

    # defines behaviour for "<"
    def __lt__(self, other):
        return Shape.centroid(self).distance_from_origin() < Shape.centroid(other).distance_from_origin()

    def centroid(self) -> Point:
        sum_x, sum_y = 0, 0
        for point in self:
            sum_x += point.x
            sum_y += point.y
        return Point(sum_x / len(self), sum_y / len(self))


p1 = Point(2.3, 43.14)
p2 = Point(5.53, 2.5)
p3 = Point(12.2, 28.7)

print(p1)
print([p1, p2, p3])

s1 = Shape(p1, p2, p3)
s2 = Shape(p2)
s3 = Shape()

print(s1)
print(s2)
print(s3)

s1 = Shape(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
s2 = Shape(Point(0, 0.5), Point(0.5, 1), Point(1, 0.5), Point(0.5, 0))
s3 = Shape(Point(0.25, 0.25), Point(0.25, 0.75), Point(0.75, 0.75), Point(0.75, 0.25))
print(s1.centroid())
print(s2.centroid())
print(s3.centroid())

p1 = Point(1, 1)
p2 = Point(5, 5)
p3 = Point(10, 10)

print(p1.distance_from_origin())
print(p2.distance_from_origin())
print(p3.distance_from_origin())

s1 = Shape(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
s2 = Shape(Point(0, 0.5), Point(0.5, 1), Point(1, 0.5), Point(0.5, 0))
print(s1 == s2)  # Equal because the two have the same centroid

s2 = Shape(Point(5, 5), Point(5, 6), Point(6, 6), Point(6, 5))

print(s1 < s2)  # s1 is smaller than s2 because its centroid is closer to the origin

s3 = Shape(Point(10, 10), Point(10, 11), Point(11, 11), Point(11, 10))
shapes = [s3, s1, s2]
print(shapes)
print(sorted(shapes))  # sorted by their distance from the origin
