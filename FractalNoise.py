#Fractalize the output of a noise source.
#Persistence is the factor by which the amplitude of the noise decreases with each successive octave
#Lacunarity is the factor by which the frequency of the noise increases with each successive octave
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