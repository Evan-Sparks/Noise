from math import *


def dot(a, b):
    if len(a) != len(b):
        raise ArithmeticError("Dot product of vectors with dimensions" + str(len(a)) + " and " + str(len(b))
                              + " is undefined")
    dp = 0
    for i in range(len(a)):
        dp += a[i] * b[i]
    return dp


def add_vector(a, b):
    return [a[i] + b[i] for i in range(len(a))]

def subtract_vector(a, b):
    return [a[i] - b[i] for i in range(len(a))]

def euclidean_distance(a, b):
    dif = subtract_vector(a, b)
    return sqrt(dot(dif, dif))

def manhattan_distance(a, b):
    reduce(lambda x, y: x + y, map(lambda x, y: abs(x - y), a, b))

def chebyshev_distance(a, b):
    reduce(max, map(lambda x, y: abs(x - y), a, b))