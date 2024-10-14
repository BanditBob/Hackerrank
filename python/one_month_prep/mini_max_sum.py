"""
"""

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))


if __name__ == "__main__":
    inputs = [
        "1 2 3 4 5",
        "256741038 623958417 467905213 714532089 938071625",
        "396285104 573261094 759641832 819230764 364801279",
        "140638725 436257910 953274816 734065819 362748590",
    ]
    for i in inputs:
        arr = list(map(int, i.split()))
        miniMaxSum(arr)
