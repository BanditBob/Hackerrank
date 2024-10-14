from cmath import phase

if __name__ == "__main__":

    n = input().strip()

    print(abs(complex(n)))
    print(phase(complex(n)))
