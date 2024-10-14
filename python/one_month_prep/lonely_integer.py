import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def lonelyinteger(a):
    # Write your code here
    counts = [(i, a.count(i)) for i in a]
    result = min(counts, key=lambda x: x[1])
    return result


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    print(result)
