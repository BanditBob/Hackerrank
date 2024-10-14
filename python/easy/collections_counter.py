from collections import Counter


def main():
    num_shoes = int(input().strip())
    inventory = Counter(input().strip().split())
    customers = int(input().strip())
    total = 0
    for i in range(customers):
        size, price = input().split()
        if inventory[size] <= 0:
            continue
        inventory[size] -= 1
        total += int(price)

    print(total)


if __name__ == "__main__":
    main()
