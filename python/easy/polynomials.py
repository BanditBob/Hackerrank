"""
polynomials.py
"""

import math
import os
import random
import re
import sys
import numpy as np


def main():
    p = list(map(float, input().split()))
    x = int(input())
    arr = np.polyval(p, x)
    print(arr)


if __name__ == "__main__":
    main()
