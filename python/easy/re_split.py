"""
re_split.py
"""

import math
import os
import random
import re
import sys

regex_pattern = r"[,.]"


def main():
    print("\n".join(re.split(regex_pattern, input())))


if __name__ == "__main__":
    main()
