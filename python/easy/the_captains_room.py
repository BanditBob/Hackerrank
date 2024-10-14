"""
the_captains_room.py
"""

import math
import os
import random
import re
import sys
from collections import Counter


def main():
    k = int(input().strip())
    n = map(int, input().strip().split())
    rooms = Counter(n)
    for room, count in rooms.items():
        if count == 1:
            print(room)


if __name__ == "__main__":
    main()
