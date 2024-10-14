def find_runner_up(n: int, arr: list) -> None:
    arr = sorted(list(set(arr)), reverse=True)
    print(arr[1])


def main():
    n = int(input())
    arr = map(int, input().split())
    find_runner_up(n, arr)


if __name__ == "__main__":
    main()
