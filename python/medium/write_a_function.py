"""
write_a_function.py
"""


def is_leap(year):
    leap = False
    mod_4, mod_100, mod_400 = [False] * 3
    if year % 4 == 0:
        mod_4 = True
    if year % 100 == 0:
        mod_100 = True
    if year % 400 == 0:
        mod_400 = True
    print(f"| {year} | {mod_4} | {mod_100} | {mod_400} |")
    # return leap


def main():
    year = int(input(">> "))
    print(f"| Year |  4  | 100 | 400 |")
    print(f"| ---: |:---:|:---:|:---:|")
    for y in range(year + 1):
        is_leap(y)


if __name__ == "__main__":
    main()
