import math
import os
import random
import re
import sys

#
# Complete the "gradingStudents" function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # grade < 40 (38 w/ rounding) is failing
    # to round up grade:
    #   within 2 points of a multiple of 5 round up
    #   > 40
    threshhold = 5
    grace_window = 2
    failing = 40
    for i, grade in enumerate(grades):
        if grade < (failing - grace_window):
            continue
        points_shy = threshhold - (grade % threshhold)
        if points_shy <= grace_window:
            grades[i] += points_shy
    return grades


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
