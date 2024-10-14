"""
exceptions.py
"""

import math
import os
import random
import re
import sys


def main():
    num_tests = int(input().strip())
    for _ in range(num_tests):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)


if __name__ == "__main__":
    main()
