def print_formatted(n: int) -> None:
    b_len = len(bin(n)[2:])
    for i in range(1, n + 1):
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        print(f"{d.rjust(b_len)} {o.rjust(b_len)} {h.rjust(b_len)} {b.rjust(b_len)}")
