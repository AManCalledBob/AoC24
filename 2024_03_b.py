""" Advent of Code 2024 """

# pylint: disable=line-too-long

import os
import re


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = str(input_file.read().splitlines())

    total = 0
    shouldadd = True
    for matches in re.finditer(r"do\(\)|don\'t\(\)|mul\((\d{1,3}+),(\d+)\)", datafile):
        print(f"Working with {matches[0]}")
        match matches[0]:
            case "do()":
                shouldadd = True
            case "don't()":
                shouldadd = False
            case _:
                if shouldadd:
                    total += int(matches[1]) * int(matches[2])

    print(f"The total is {total}")


if __name__ == "__main__":
    main()
