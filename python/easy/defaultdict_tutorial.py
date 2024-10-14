"""
defaultdict_tutorial.py
"""

# from collections import defaultdict
# def main():
#     d = defaultdict(list)
#     a, b = map(int, input().split())
#     print(d)
#     for i in range(a):
#         user_input = input()
#         d[user_input]
#         # d.get(user_input).append(i + 1)
#     for _ in range(b):
#         user_input = input()
#         print(d.get(user_input) or -1)
# if __name__ == "__main__":
#     main()
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for _ in range(n):
    d["A"].append(input())
B = []
for _ in range(m):
    B.append(input())
for item in B:
    if item in d["A"]:
        result = [i + 1 for i, x in enumerate(d["A"]) if x == item]
        print(*result)
    else:
        print(-1)
