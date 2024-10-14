import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    x, y = [0, 0]
    for i, a in enumerate(arr):
        b = list(reversed(a))
        x += a[i]
        y += b[i]
    return abs(x - y)


def main():
    # n = int(input(">> ").split())
    arr = [[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]]
    result = diagonalDifference(arr)
    print(result)
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)
    print(result)


if __name__ == "__main__":
    main()
