"""
collections_deque.py
"""

from collections import deque


def main():
    n = int(input().strip())
    d = deque()
    for _ in range(n):
        c, *v = input().strip().split()
        if v == []:
            v = None
        else:
            v = int(v.pop())
        try:
            func = getattr(d, c)
            if c.startswith("append"):
                func(v)
            else:
                func()
        except AttributeError:
            print(f"{c} not found")
    temp = list(map(str, list(d)))
    print(temp)


if __name__ == "__main__":
    main()
    # tasks = [
    #     "append 1",
    #     "append 2",
    #     "append 3",
    #     "appendleft 4",
    #     "pop",
    #     "popleft",
    # ]
