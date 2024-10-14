"""
symmetric_difference.py
"""

import math
import os
import random
import re
import sys


def main():
    m = int(input().strip())
    e = map(int, input().strip().split())
    n = int(input().strip())
    f = map(int, input().strip().split())
    e, f = set(e), set(f)
    print(len(e.union(f) - e.intersection(f)))


if __name__ == "__main__":
    main()
