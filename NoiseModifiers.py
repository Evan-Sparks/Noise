from PerlinNoise3d import *


class NormalizedPerlin3d:
    def __init__(self):
        self.delegate = Clamp(Scale(PerlinNoise3d(), 1.742), 1, -1)
        
    def noise(self, point):
        return self.delegate.noise(point)


class Clamp:
    def __init__(self, delegate, upper_bound, lower_bound=0):
        self.delegate = delegate
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def noise(self, point):
        return max(self.lower_bound, min(self.upper_bound, self.delegate.noise(point)))


class Scale:
    def __init__(self, delegate, factor):
        self.delegate = delegate
        self.factor = factor

    def noise(self, point):
        return self.delegate.noise(point) * self.factor


class Abs:
    def __init__(self, delegate):
        self.delegate = delegate

    def noise(self, point):
        return abs(self.delegate.noise(point))


class Apply:
    def __init__(self, delegate, func):
        self.delegate = delegate
        self.func = func

    def noise(self, point):
        return self.func(self.delegate.noise(point))


class Combine:
    def __init__(self, source_one, source_two, combiner):
        self.source_one = source_one
        self.source_two = source_two
        self.combiner = combiner

    def noise(self, point):
        return self.combiner(self.source_one.noise(point), self.source_two.noise(point))


class ApplyToPoint:
    def __init__(self, func):
        self.func = func

    def noise(self, point):
        return self.func(point)