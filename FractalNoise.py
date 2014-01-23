class FracalNoise:
    def __init__(self, delegate, octaves=3, persistence=0.5, lacunarity=2):
        self.delegate = delegate
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity

    def noise(self, point):
        value = 0
        for i in range(1, self.octaves + 1):
            value += self.delegate.noise(map(lambda x: x * (self.lacunarity ** (i - 1)), point)) \
                * (self.persistence ** (i - 1))
        return value