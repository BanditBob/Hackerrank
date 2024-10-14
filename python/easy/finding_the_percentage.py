def calculate_average(grades: list):
    return sum(grades) / len(grades)


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    result = calculate_average(student_marks.get(query_name))
    print(f"{result:.2f}")
