"""
check_strict_superset.py
"""


def main():
    a = set(map(int, input().split()))
    n = int(input())
    check = True
    for _ in range(n):
        s = set(map(int, input().split()))
        print((a.issuperset(s) and a != s))
        # if not (a.issuperset(s) and a != s):
        #     check = False
        #     break
    print(check)


if __name__ == "__main__":
    main()
