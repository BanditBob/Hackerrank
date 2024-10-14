def main():
    c = "H"
    n = int(input())
    t_b = int(n + 1)
    mid = int(t_b / 2)
    pad = int(n - mid)
    display = []
    for i in range(n):
        output = c * (2 * i + 1)
        display.append(output.center((2 * n - 1)))
    for i in range(t_b):
        output = (c * n) + (" " * (n * 3)) + (c * n)
        display.append(output.rjust(len(output) + pad))
    for i in range(mid):
        output = c * (n * 5)
        display.append(output.rjust(len(output) + pad))
    for i in range(t_b):
        output = (c * n) + (" " * (n * 3)) + (c * n)
        display.append(output.rjust(len(output) + pad))
    for i in range(n - 1, -1, -1):
        output = c * (2 * i + 1)
        output = (" " * (n * 4)) + output.center(2 * n - 1)
        display.append(output)
    for i in display:
        print(i)


if __name__ == "__main__":
    main()
