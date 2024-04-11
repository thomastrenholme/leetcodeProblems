import sys

## https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
class Solution:

    def __init__(self):
        self.nearestValidPointIndex = -1
        self.nearestValidPointDistance = sys.maxsize
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:

        for i in range(0, len(points)):

            pointX = points[i][0]
            pointY = points[i][1]

            if not (x == pointX or y == pointY):
                continue

            distance = abs(x - pointX) + abs(y - pointY)

            if distance < self.nearestValidPointDistance:
                self.nearestValidPointIndex = i
                self.nearestValidPointDistance = distance

        return self.nearestValidPointIndex
