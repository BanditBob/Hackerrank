from itertools import product

if __name__ == "__main__":
    n = input().split()
    m = input().split()
    x = []
    x.append([int(i) for i in n])
    x.append([int(i) for i in m])
    x = list(product(*x))
    for i in x:
        print(i, end=" ")
