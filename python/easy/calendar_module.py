"""
calendar_module.py
"""

import calendar


def main():
    day_names = list(calendar.day_name)
    m, d, y = map(int, input().split())
    print(day_names[calendar.weekday(y, m, d)].upper())


if __name__ == "__main__":
    main()
