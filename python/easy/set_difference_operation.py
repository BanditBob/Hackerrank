"""
set_difference_operation.py
"""

import math
import os
import random
import re
import sys


def main():
    m = int(input().strip())
    a = map(int, input().strip().split())
    n = int(input().strip())
    b = map(int, input().strip().split())
    a, b = set(a), set(b)
    print(len(a - b))


if __name__ == "__main__":
    main()
