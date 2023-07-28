from math import asin, pi
import numpy as np

dirs = [
    [ 1., 0., 0.],
    [-1., 0., 0.],
    [0.,  1., 0.],
    [0., -1., 0.],
    [0., 0.,  1.],
    [0., 0., -1.],
]

for _ in range(1_000):
    v = np.random.normal(size=3)
    v /= np.linalg.norm(v)

    sum = 0.0
    for [x, y, z] in dirs:
        dot = x * v[0] + y * v[1] + z * v[2]
        pos = dot > 0.0
        sum += dot * dot * pos
        

    print("final sum:", sum)

