def make_list(a: int, b: int, c: int, num: int):
    rx, ry, rz = list(range(a + 1)), list(range(b + 1)), list(range(c + 1))
    all_perms = [[x, y, z] for x in rx for y in ry for z in rz if sum([x, y, z]) != num]
    print(all_perms)


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    make_list(x, y, z, n)


if __name__ == "__main__":
    main()
