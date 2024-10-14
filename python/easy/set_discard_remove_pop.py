n = int(input())
N = input()
set_of_numbers = set(map(int, N.split()))
Number_of_commands = int(input())
for _ in range(Number_of_commands):
    command = input()
    if "pop" in command:
        if len(set_of_numbers) > 0:
            set_of_numbers.pop()
    elif "remove" in command:
        num_to_remove = int(command.split()[1])
        if num_to_remove in set_of_numbers:
            set_of_numbers.remove(num_to_remove)
    elif "discard" in command:
        num_to_discard = int(command.split()[1])
        set_of_numbers.discard(num_to_discard)
print(sum(set_of_numbers))
