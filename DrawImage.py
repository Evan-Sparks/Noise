__author__ = 'Evan'
from PIL import Image
from NoiseModifiers import *
from FractalNoise import *


def draw_image(source, width=1024, height=512, name="test.png", scale=10):
    i = Image.new("RGB", (width, height), "white")
    for x in range(1024):
        for y in range(512):
            pos = [scale * float(x)*2 / 512.0, scale * height / width * float(y)*2 / 512.0, 0.33]
            v = int(source.noise(pos))
            i.putpixel((x, y), (v, v, v))
    i.save(name)


if __name__ == "__main__":
    n = Apply(Scale(NormalizedPerlin3d(), 128), lambda x: x + 128)
    draw_image(n, name="Examples/Noise.png")
    n = Apply(Scale(FracalNoise(PerlinNoise3d()), 128), lambda x: x + 128)
    draw_image(n, name="Examples/FractalNoise.png")
    n = Scale(Abs(FracalNoise(PerlinNoise3d())), 400)
    draw_image(n, name="Examples/AbsFractalNoise.png")
    n = Apply(Scale(Apply(Combine(ApplyToPoint(lambda x: x[0]), FracalNoise(Abs(PerlinNoise3d())),
                                  (lambda x, y: x + y)), sin), 128), lambda x: x + 128)
    draw_image(n, name="Examples/Stripes.png")