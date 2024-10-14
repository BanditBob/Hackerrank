"""
arrays.py
"""

import numpy as np


def arrays(arr):
    # complete this function
    # use numpy.array
    return np.array(arr)[::-1]


arr = input().strip().split(" ")
result = arrays(arr)
print(result)
