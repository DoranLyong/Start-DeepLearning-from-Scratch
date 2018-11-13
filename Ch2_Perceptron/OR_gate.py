import numpy as np


def OR(x1, x2):
    x = np.array([x1, x2])   # input
    w = np.array([0.5, 0.5]) # weight
    b = -0.2                   # bias

    temp = np.sum(w*x) + b

    if temp <= 0:
        return 0
    else:
        return 1
