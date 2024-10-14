"""
collections_ordereddict.py
"""

from collections import OrderedDict


def main():
    n = int(input())
    purchases = OrderedDict()
    for _ in range(n):
        *s, n = input().split()
        s = " ".join(s)
        purchases.setdefault(s, 0)
        purchases[s] += int(n)
    for k, v in purchases.items():
        print(k, v)


if __name__ == "__main__":
    main()
