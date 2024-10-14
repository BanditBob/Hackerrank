"""
linear_algebra.py
"""

import numpy as np


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(float, input().split())))
    print(round(np.linalg.det(np.array(a)), 3))


if __name__ == "__main__":
    main()
