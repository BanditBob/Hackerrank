# Complete the solve function below.

import re


def solve(s):
    def to_title_case(match):
        return match.group(0).capitalize()

    return re.sub(r"\b\w", to_title_case, s)
