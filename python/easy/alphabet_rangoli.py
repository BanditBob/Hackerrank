import string


def print_rangoli(n):
    letters = string.ascii_lowercase[:n]
    display = []
    for i in range(len(letters), 0, -1):
        x = letters[i - 1 :]
        if len(x) > 1:
            x = list(reversed(x[1::])) + list(x)
            x = "-".join(x)
        display.append(x)
    width = len(display[-1])
    display = display + list(reversed(display[0:-1]))
    for i in display:
        print(i.center(width, "-"))
