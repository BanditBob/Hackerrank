"""
Subarray Division
"""

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    c, i = 0, 0
    while m + i <= len(s):
        c += 1 * (sum(s[i : i + m]) == d)
        i += 1
    return c


if __name__ == "__main__":
    s = list(map(int, input().strip().split()))
    d, m = list(map(int, input().strip().split()))
    result = birthday(s, d, m)
    print(result)
