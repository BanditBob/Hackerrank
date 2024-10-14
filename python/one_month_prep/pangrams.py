import math
import os
import random
import re
import string
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    # Write your code here
    x = set(sorted(s.lower().replace(" ", "")))
    if all([(s in x) for s in string.ascii_lowercase]):
        return "pangram"
    else:
        return "not pangram"


if __name__ == "__main__":
    tests = [
        "We promptly judged antique ivory buckles for the next prize",
        "We promptly judged antique ivory buckles for the prize",
    ]
    result = None
    for t in tests:
        result = pangrams(t)
