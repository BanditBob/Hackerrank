"""
incorrect_regex.py
"""

import math
import os
import random
import re
import sys

tests = [
    [r".*\+", r".*+"],
    [r"[0-9]++", r"[0-9]", r"123"],
    [r"/^(?!\.)(?=.)[d-\.]$/", r"[a-zA-Z0-9,.' ]+"],
]


def main():
    #     t = int(input().strip())
    for test in tests:
        print()
        for t in test:
            # print(t)
            try:
                # print(re.compile(t))
                print(True)
            except re.error:
                print(False)
            # print(f"{t}", re.compile(t))
    # for i in range(t):
    #     s = input().strip()
    #     print(re.compile(s))
    #     # try:
    #     #     re.compile(s)
    #     #     print(True)
    #     # except:
    #     #     print(False)


if __name__ == "__main__":
    main()
