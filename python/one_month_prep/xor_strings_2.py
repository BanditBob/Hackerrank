"""
"""

import math
import os
import random
import re
import sys


def main():
    a = abs(int(input().strip(), base=2))
    b = abs(int(input().strip(), base=2))
    print(f"{a ^ b:b}".zfill(len(f"{a:b}")))


if __name__ == "__main__":
    main()
