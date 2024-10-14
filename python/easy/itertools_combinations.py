from itertools import combinations


def main():
    s = input().strip().split()
    l, c = list(s[0]), int(s[1])
    combos = []
    for i in range(1, c + 1):
        combos = combos + list(combinations(sorted(l), i))
    for x in combos:
        print("".join(x))


if __name__ == "__main__":
    main()
