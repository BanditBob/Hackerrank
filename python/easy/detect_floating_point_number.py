"""
introduction_to_regex.py
"""

import math
import os
import random
import re
import sys


def main():
    pattern = re.compile(r"^[+-]?\d*(\.\d*)$")
    results = []
    T = int(input().strip())
    for _ in range(T):
        n = input().strip()
        results.append(bool(pattern.match(n)))
    for x in results:
        print(x)


if __name__ == "__main__":
    main()
