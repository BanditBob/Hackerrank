def main():
    h, w = input().strip().split()
    h, w = int(h), int(w)
    message = "WELCOME"
    pat_temp = ".|."
    display = []
    display.append(message.center(w, "-"))
    for i in range(h // 2, 0, -1):
        output = pat_temp * (i * 2 - 1)
        display.insert(0, output.center(w, "-"))
        display.append(output.center(w, "-"))
    for x in display:
        print(x)


if __name__ == "__main__":
    main()
