"""
map_and_lambda_function.py
"""

import math
import os
import random
import re
import sys

cube = lambda x: x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append((sum(fib_seq[-2:])))
    return fib_seq


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
