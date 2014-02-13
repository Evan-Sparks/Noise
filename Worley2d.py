from VectorOps import *
import random


class Worley2d:
    def __init__(self, seed=0, cells_per_unit=1, distance=euclidean_distance, combiner=None, points_to_combine=3):
        self.seed = seed
        self.cells_per_unit = cells_per_unit
        self.distance = distance
        self.points_to_combine = points_to_combine
        self.combiner = combiner
        if self.combiner is None:
            self.combiner = self.closest_combiner

    def noise(self, point):
        xint = int(point[0]) % 256
        yint = int(point[1]) % 256
        point_off = [point[0] - xint, point[1] - yint]
        dists = []
        for xoff in [-1, 0, 1]:
            for yoff in [-1, 0, 1]:
                r = random.Random()
                r.seed(self._hash(xint + xoff, yint + yoff))
                for i in range(self.cells_per_unit):
                    dist = self.distance([xoff + r.uniform(0, 1), yoff + r.uniform(0, 1)], point_off)
                    dists = self._dist_helper(dists, dist)
        return self.combiner(dists)

    @staticmethod
    def closest_combiner(points):
        return points[0]

    def _hash(self, x, y):
        return 31 * (31 * x + y) + self.seed

    def _dist_helper(self, dists, dist):
        dists.append(dist)
        dists.sort()
        if len(dists) > self.points_to_combine:
            dists.pop(-1)
        return dists
