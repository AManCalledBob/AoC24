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

    # Consume between don't and do
    result = str(re.sub(r"don't.*?do", "", datafile, 0))

    matches = re.findall(r"mul\(\d+,\d+\)", result)

    subtotal = 0
    for eachmatch in matches:
        left, right = eachmatch[4:-1].split(",")
        subtotal += int(left) * int(right)
    print(f"The total is {subtotal}")


if __name__ == "__main__":
    main()
