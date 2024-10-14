"""
check_subset.py
"""

import math
import os
import random
import re
import sys


def main():
    t = int(input().strip())
    for _ in range(t):
        num_a = int(input().strip())
        a = set(map(int, input().split()))
        num_b = int(input())
        b = set(map(int, input().split()))
        print(bool(len(b.intersection(a)) == num_a))


if __name__ == "__main__":
    main()
