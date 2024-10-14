#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    if all([(sum(c) >= k) for c in zip(A, B)]):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    q = 2
    n, k = [3, 10]
    A = [2, 1, 3]
    B = [7, 8, 9]
    result = twoArrays(k, A, B)
    print(result)
    n, k = [4, 5]
    A = [1, 2, 2, 1]
    B = [3, 3, 3, 4]
    result = twoArrays(k, A, B)
    print(result)
    q = 1
    n, k = [5, 10]
    A = [7, 6, 8, 4, 2]
    B = [5, 2, 6, 3, 1]
    result = twoArrays(k, A, B)
    print(result)
