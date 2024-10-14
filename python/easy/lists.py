def main():
    user_list = list()
    n = int(input())
    for _ in range(N):
        user_cmd = input().strip()
        parts = user_cmd.split()
        match parts[0]:
            case "print":
                print(user_list)
            case "insert":
                user_list.insert(int(parts[1]), int(parts[2]))
            case "remove":
                user_list.remove(int(parts[1]))
            case "append":
                user_list.append(int(parts[1]))
            case "sort":
                user_list.sort()
            case "reverse":
                user_list.reverse()
            case "pop":
                user_list.pop()


if __name__ == "__main__":
    main()
