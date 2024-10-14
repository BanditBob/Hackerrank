def main():
    my_set = set()
    n = int(input())
    for _ in range(n):
        user_input = input()
        my_set.add(user_input)
    print(len(list(my_set)))


if __name__ == "__main__":
    main()
