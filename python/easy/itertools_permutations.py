from itertools import permutations


def main():
    s = input().strip().split()
    l, c = list(s[0]), int(s[1])
    combos = list(permutations(l, c))
    for x in list(sorted(combos)):
        print("".join(x))


if __name__ == "__main__":
    main()
