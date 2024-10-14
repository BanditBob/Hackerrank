from itertools import groupby


def main():
    user_input = input().strip()
    groups = [(len(list(g)), int(k)) for k, g in groupby(user_input)]
    for g in groups:
        print(g, end=" ")


if __name__ == "__main__":
    main()
