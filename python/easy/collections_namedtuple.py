"""
collections_namedtuple.py
"""

from collections import namedtuple


def main():
    n, cols = int(input()), input().split()
    idx = cols.index("MARKS")
    t = 0
    for _ in range(n):
        Student = namedtuple("Student", "mark")
        s = Student(mark=int(input().split()[idx]))
        t += s.mark
    print(round(sum(t) / n, 2))


if __name__ == "__main__":
    main()
