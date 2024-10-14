import numpy as np


def main():
    matrix = []
    user_input = input().strip()
    rows, cols = [int(x) for x in user_input.split()]
    for i in range(rows):
        user_input = input().strip()
        user_input = [int(x) for x in user_input.split()]
        matrix.append(user_input)
    my_array = np.array(matrix)
    my_array = np.sum(my_array, axis=0)
    print(np.prod(my_array, axis=0))


if __name__ == "__main__":
    main()
