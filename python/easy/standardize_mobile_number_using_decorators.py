"""
standardize_mobile_number_using_decorators.py
"""

import math
import os
import random
import re
import sys

tests = ["07895462130", "919875641230", "9195969878"]


def wrapper(f):
    def fun(l):
        pass

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")


def main():
    pass


if __name__ == "__main__":
    main()
