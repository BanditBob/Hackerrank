"""
mod_divmod.py
"""

import math
import os
import random
import re
import sys


def main():
    a = int(input().strip())
    b = int(input().strip())
    m, d = divmod(a, b)
    print(m)
    print(d)
    print(divmod(a, b))


if __name__ == "__main__":
    main()
