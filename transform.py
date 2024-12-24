import numpy as np
import math as m

def translate(dx: float, dy: float):
    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [dx, dy, 1]
    ])

def scale(sx: float, sy: float):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def rotate(angle: float):
    cs = m.cos(angle)
    sn = m.sin(angle)
    return np.array([
        [cs, sn, 0],
        [-sn, cs, 0],
        [0, 0, 1]
    ])

