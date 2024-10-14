import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    h, x = int(s[:2]), s[-2:]
    h = h % 12
    if x == "PM":
        h += 12
    return str(h).zfill(2) + s[2:-2]


if __name__ == "__main__":
    tests = ["06:40:03AM", "12:40:22AM", "07:05:45PM", "12:05:39AM", "02:34:50PM"]
    for t in tests:
        print(timeConversion(t))
