"""
any_or_all.py
"""

import math
import os
import random
import re
import sys


def main():
    n = int(input())
    l = list(map(int, input().strip().split()))
    if all([(x > 0) for x in l]):
        if any((str(x) == str(x)[::-1]) for x in l):
            print(True)
        else:
            print(False)
    else:
        print(False)


if __name__ == "__main__":
    main()
