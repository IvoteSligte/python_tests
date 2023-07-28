from itertools import chain
import numpy as np
import fibonacci_sphere

bands = [
    [
        lambda x, y, z: 0.28209479,
    ],
    [
        lambda x, y, z: 0.48860251 * y,
        lambda x, y, z: 0.48860251 * z,
        lambda x, y, z: 0.48860251 * x,
    ],
    [
        lambda x, y, z: 1.09254843 * x * y,
        lambda x, y, z: 1.09254843 * y * z,
        lambda x, y, z: 0.31539156 * (3 * z * z - 1),
        lambda x, y, z: 1.09254843 * x * z,
        lambda x, y, z: 0.54627421 * (x * x - y * y),
    ]
]


def desired_fn(x: float, y: float, z: float) -> float:
    return max(z, 0.0)


def eval_first_band(x: float, y: float, z: float, c1: float) -> float:
    return bands[0][0](x, y, z) * c1


def eval_second_band(x: float, y: float, z: float, c2s: list[float]) -> float:
    t = 0.0
    for func, coef in zip(bands[1], c2s):
        t += func(x, y, z) * coef
    return t


eval_first_order = eval_first_band


def eval_second_order(x: float, y: float, z: float, c1: float, c2s: list[float]) -> float:
    return eval_first_band(x, y, z, c1) + eval_second_band(x, y, z, c2s)


orders = [eval_first_band, eval_second_band]

num_points = 1_000_000

points = fibonacci_sphere.fibonacci_sphere(num_points)

coefs = np.array([0.0 for _ in range(9)])


def change(received: float, expected: float) -> float:
    return 0 if received == 0 else expected / received


def calc_first_band() -> float:
    c1 = 0.0
    for (x, y, z) in points:
        desired = desired_fn(x, y, z)
        t1 = change(bands[0][0](x, y, z), desired)
        c1 += t1
    c1 /= num_points
    return c1


def calc_second_band(c1: float) -> list[float]:
    c2s = [0.0, 0.0, 0.0]
    for (x, y, z) in points:
        t1 = eval_first_order(x, y, z, c1)
        desired = desired_fn(x, y, z) - t1
        for m, band_fn in enumerate(bands[1]):
            t2 = change(band_fn(x, y, z), desired)
            c2s[m] += t2
    return list(np.array(c2s) / num_points)


def calc_third_band(c1: float, c2s: list[float]) -> list[float]:
    c3s = [0.0, 0.0, 0.0, 0.0, 0.0]
    for (x, y, z) in points:
        t2 = eval_second_order(x, y, z, c1, c2s)
        desired = desired_fn(x, y, z) - t2
        for m, band_fn in enumerate(bands[2]):
            t3 = change(band_fn(x, y, z), desired)
            c3s[m] += t3
    return list(np.array(c3s) / num_points)


calc_first_order = calc_first_band


def calc_second_order() -> list[float]:
    c1 = calc_first_order()
    c2s = calc_second_band(c1)
    return [c1] + c2s


def calc_third_order() -> list[float]:
    c1 = calc_first_order()
    c2s = calc_second_band(c1)
    c3s = calc_third_band(c1, c2s)
    return [c1] + c2s + c3s


print(calc_third_order())
