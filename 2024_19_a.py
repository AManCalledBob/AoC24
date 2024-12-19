""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import operator
import re

from collections import deque


def main():
    """Main Function"""

    towel = list()
    total = 0

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    for item in datafile[0].split(", "):
        towel.append(item)
    towel = sorted(towel, key=len, reverse=True)

    restring = r""
    for item in towel:
        restring = restring + "|" + item
    restring = "/" + restring[1:]

    for design in datafile[2:]:
        print(f"Working on {design} with {restring}")

        x = re.match(restring, design)
        if x is None:
            print(f"{design} is not possible")
        else:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
