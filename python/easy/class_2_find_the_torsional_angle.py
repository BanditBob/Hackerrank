"""
class_2_find_the_torsional_angle.py
"""

import math

# tests = [
#     ["0 4 5", "1 7 6", "0 5 9", "1 7 2"],
#     ["5 8.8 9", "4 -1 3", "7 8.7 3.3", "4.4 5.1 6.3"],
# ]


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x,
        )

    def absolute(self):
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)


if __name__ == "__main__":
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)
    a, b, c, d = (
        Points(*points[0]),
        Points(*points[1]),
        Points(*points[2]),
        Points(*points[3]),
    )
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))
