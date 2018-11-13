import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])     # input
    w = np.array([0.5,0.5])   # weight
    b = -0.7                    # bias

    temp = np.sum(w*x) + b # y = w1x1 + w2x2 + b

    if temp <= 0:
        return 0
    else:
        return 1
