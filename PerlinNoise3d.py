from VectorOps import *
from random import *
from math import *


#A simple implementation of Ken Perlin's original noise algorithm
class PerlinNoise3d:
    def __init__(self, s=0):
        seed(s)
        self.grad_gen = PerlinGrad83()

    def noise(self, point):
        grid_base = map(floor, point)
        point_offset = [point[i] - grid_base[i] for i in range(3)]

        yz0 = exp_easing(self._vertex_weight(grid_base, point),
                         self._vertex_weight(add_vector(grid_base, [1, 0, 0]), point),
                         point_offset[0])
        yz1 = exp_easing(self._vertex_weight(add_vector(grid_base, [0, 1, 0]), point),
                         self._vertex_weight(add_vector(grid_base, [1, 1, 0]), point),
                         point_offset[0])
        yz2 = exp_easing(self._vertex_weight(add_vector(grid_base, [0, 0, 1]), point),
                         self._vertex_weight(add_vector(grid_base, [1, 0, 1]), point),
                         point_offset[0])
        yz3 = exp_easing(self._vertex_weight(add_vector(grid_base, [0, 1, 1]), point),
                         self._vertex_weight(add_vector(grid_base, [1, 1, 1]), point),
                         point_offset[0])

        z0 = exp_easing(yz0, yz1, point_offset[1])
        z1 = exp_easing(yz2, yz3, point_offset[1])

        return exp_easing(z0, z1, point_offset[2])

    def _vertex_weight(self, vertex, point):
        grad = self.grad_gen.vertex_grad(vertex)
        return dot(grad, [point[k] - vertex[k] for k in range(3)])


#A simple exponential easing interpolation function
def exp_easing(a, b, t):
    return a - (3 * t ** 2 - 2 * t ** 3) * (a - b)


#A class to generate pseudorandom 3d gradient vectors of magnitude 1, based on Ken Perlin's original 1983 algorithm
class PerlinGrad83:
    def __init__(self, size=256):
        self.size = size
        self.perms = range(self.size)
        shuffle(self.perms)
        self.grads = []
        while len(self.grads) < self.size:
            vector = [uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]
            magnitude = sqrt(dot(vector, vector))
            if magnitude < 1:
                self.grads.append([vector[0] / magnitude, vector[1] / magnitude, vector[2] / magnitude])

    def vertex_grad(self, vertex):
        return self.grads[int((vertex[0] +
                               self.perms[int((vertex[1] + self.perms[int(vertex[2] % self.size)]) % self.size)])
                              % self.size)]
