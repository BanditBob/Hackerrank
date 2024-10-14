"""
CREATED: October 13, 2024
Hackerrank/update_files.py
"""
import json
import os
import shutil
from itertools import zip_longest

import black
from rich import inspect, print


def main():
    subs = dict()
    dir_files = list(os.walk("D:\\Hackerrank\\python"))


    dupes = dict()

    for r, d, fs in dir_files:
        for x in fs:
            dupes.setdefault(x, [])
            dupes[x].append(r)
    dupes = {k: v for k,v in dupes.items() if len(v) > 1}


    for file, paths in dupes.items():
        # contents = [(p + os.sep + file, open(p + os.sep + file, "r", encoding="utf-8").read().rstrip()) for p in paths]
        contents = [open(p + os.sep + file, "r", encoding="utf-8") for p in paths]
        # print(contents)

        lengths = [len(c.read().rstrip()) for c in contents]
        if any(lengths):

            print(lengths)
            complete = contents[lengths.index(max(lengths))].name
            for c in contents:
                if c.name == complete:
                    continue
                shutil.copy(complete, c.name)
                # print(contents(max(lengths))]
                # print(lengths.index(max(lengths)))
                # print(c.name)
            # print("=" * 120)
        # for x in contents:
        #     print(repr(x.readlines()))


            # if os.path.getsize(r + os.sep + x) < 8:
            #     continue
            # content = []
            # with open(r + os.sep + x, "r", encoding="utf-8") as f:
            #     content = [l.rstrip() for l in f.readlines()]
            # print(f"{r + os.sep + x}")
            # for c in content:
            #     # if c.startswith("\n"):
            #     #     c = c[1:]
            #     print(c)
            # print("=" * 80)

    # with open("./banditbob_1995/2024_10_13_data.json", "r", encoding="utf-8") as f:
    #     subs = json.loads(f.read())

    # subs_list = []

    # for sub in subs["submissions"]:
    #     if sub["score"] < 1.0 or sub["language"] == "javascript":
    #         continue
    #     del sub["language"]
    #     subs_list.append(sub)

    # for item in subs_list:

    #     name = ""
    #     for l in item["challenge"]:
    #         if l.isalpha() or l.isspace():
    #             name += l.lower()
    #         elif l == ".":
    #             name += " "
    #         elif l.isnumeric():
    #             name += f" {l.lower()}"
    #         else:
    #             name += ""
    #     name = "_".join(name.split()) + ".py"

    #     # print(name.center(200, "="))
    #     for r, d, fs in dir_files:
    #         if name not in fs:
    #             continue
    #         full_path = r + os.sep + name
    #         file_header = f'"""\n{r + os.sep + name}\n"""'
    #         contents = None
    #         split_str = "\n"
    #         output = item["code"].split(split_str)
    #         output = [p[1:] if p.startswith("\n") else p for p in item["code"].split(split_str)]

    #         with open(full_path, "r", encoding="utf-8") as f:
    #             contents = f.read()
    #             contents = [p[1:] if p.startswith("\n") else p for p in f.read().split(split_str)]

    #         comparison = list(zip_longest(contents, output, fillvalue=""))


    #         print(full_path)
            # print("\n" + name.center(200, "=") + "\n")
            # for o, n in comparison:
                # if n.startswith("\n"):
                #     n = "".join(n[1:])
                # print(f"{repr(o)}")
                # print(f"{repr(n)}")
                # print(f"{o:<100}|{n:<100}")
                # print(repr(n))

            # for x in comparison:
                # print(x)
                # old_line = old_line.replace("==  ", "== ")
                # if old_line == new_line:
                # print("-" * 120)
                # print(repr(old_line))
                # print(repr(new_line))

                # print(old_line == new_line)
                # print(repr(old_line) == repr(new_line), repr(old_line), repr(new_line))

            # for x in list(enumerate(output)):
            #     print(x)


            # file_header = f'"""\n{name}\n"""'

            # print(f"Fixing: {r + os.sep + name}")

            # with open(f"{r + os.sep + name}", "w", encoding="utf-8") as f:
            #     output = item["code"]
            #     if not output.startswith(file_header):
            #         output = f'{file_header}\n\n' +  item["code"]
            #     f.write(output)
                # print(output)

                # print("Replaced: " + repr(old_contents))
                # print("With:     " + repr(output))


            # print(x["challenge"], x["code"])
        # name = x["challenge"]
        # print(name)

if __name__ == "__main__":
    os.system("cls")
    main()
    # dir_files = list(os.walk("D:\\Hackerrank\\python"))
    # for r, d, fs in dir_files:
    #     for f in fs:
    #         content = []
    #         with open(r + os.sep + f, "r", encoding="utf-8") as f:
    #             # parts = [p.replace("\n", " ") for p in f.read().split("\n\n")]
    #             # parts = [p[1:] if p.startswith("\n") else p for p in f.read().split("\n\n")]
    #             print(f.read())
