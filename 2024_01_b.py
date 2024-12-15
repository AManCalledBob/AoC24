""" Advent of Code 2024 """

# pylint: disable=line-too-long

import os

left_list = []
right_list = []


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0]}_input_data.txt", encoding="utf-8"
    ) as input_file:
        # datastream = list(map(int, input_file.read().splitlines()))
        datastream = input_file.read().splitlines()

    running_total = 0
    for oneline in datastream:
        left, right = oneline.split()
        left_list.append(int(left))
        right_list.append(int(right))

    for item, value in enumerate(left_list):
        running_total += abs(value * right_list.count(value))
    print(running_total)


if __name__ == "__main__":
    main()
