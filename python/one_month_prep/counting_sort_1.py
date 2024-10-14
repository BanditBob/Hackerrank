"""
"""

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    x = [0] * 100
    for i in arr:
        x[i] += 1
    return x


if __name__ == "__main__":
    tests = [
        "./inputs/counting_sort_100.txt",
        # "./inputs/counting_sort_1000.txt",
        # "./inputs/counting_sort_10000.txt",
        # "./inputs/counting_sort_100000.txt",
    ]
    for t in tests:
        with open(t, "r") as file:
            lines = [line.strip() for line in file]
            n, arr = int(lines[0]), list(map(int, lines[1].split()))
            result = countingSort(arr)
            [print(str(r), end=" ") for r in result]
            # print(" ".join(result))
