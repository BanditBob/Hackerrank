"""
set_mutations.py
"""

import math
import os
import random
import re
import sys


def main():
    m = int(input().strip())
    a = set(map(int, input().strip().split()))
    n = int(input().strip())
    for _ in range(n):
        c, v = input().split()
        s = set(map(int, input().strip().split()))
        if c == "intersection_update":
            a.intersection_update(s)
        elif c == "update":
            a.update(s)
        elif c == "symmetric_difference_update":
            a.symmetric_difference_update(s)
        elif c == "difference_update":
            a.difference_update(s)
        else:
            raise ValueError
    print(sum(a))


if __name__ == "__main__":
    main()
