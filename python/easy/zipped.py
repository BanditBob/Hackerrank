"""
zipped.py
"""

tests = ["89 90 78 93 80", "90 91 85 88 86", "91 92 83 89 90.5"]


def main():
    all_grades = []
    for test in tests:
        test = list(map(float, test.split()))
        all_grades.append(test)
    for g in zip(*all_grades):
        print(sum(g) / len(g))
    # n, x = input().strip().split()
    # all_grades = []
    # for i in range(int(x)):
    #     grades = list(map(float, input().strip().split()))
    #     all_grades.append(grades)
    # all_grades = zip(*all_grades)
    # print(all_grades)


if __name__ == "__main__":
    main()
