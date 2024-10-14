"""
Computes the average of a list of numbers
"""


def average(array):
    # your code goes here
    return sum(set(array)) / len(set(array))
