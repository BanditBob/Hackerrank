def get_second_lowest(grades: list) -> None:
    pts = {}
    for entry in grades:
        name, grade = entry
        pts.setdefault(grade, [])
        pts.get(grade).append(name)
    ordered = sorted(list(pts.keys()))
    for i in sorted(pts.get(ordered[1])):
        print(i)


def main():
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
    get_second_lowest(grades)


if __name__ == "__main__":
    main()
