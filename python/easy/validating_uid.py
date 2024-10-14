def validate_uid(id: str) -> bool:
    # 10 chars long
    if len(id) != 10:
        return False
    # All unique characters
    if len(set(id)) != len(id):
        return False
    # All alphanumeric
    if not id.isalnum():
        return False
    # More than 3 numbers
    if (sum(1 for c in id if c.isnumeric())) < 3:
        return False
    # More than 2 uppercase letters
    if (sum(1 for c in id if c.isupper())) < 2:
        return False
    return True


def main():
    n = int(input().strip())
    uids = []
    for i in range(n):
        user_input = input().strip()
        uids.append(user_input)
    for id in uids:
        result = validate_uid(id)
        if result:
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
