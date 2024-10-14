"""
input.py
"""

import math
import os
import random
import re
import sys


def main():
    x, k = list(map(int, input().strip().split()))
    p = eval(input())
    print(p == k)


if __name__ == "__main__":
    main()
