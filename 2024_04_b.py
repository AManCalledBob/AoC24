""" Advent of Code 2024 """

# pylint: disable=line-too-long

import os

searchstring = "XMAS"


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    found_count = 0
    width = len(datafile[0])
    height = len(datafile)

    p1 = 0
    height = len(datafile)
    width = len(datafile[0])
    for y in range(height - 2):
        for x in range(width - 2):
            s1 = datafile[y][x] + datafile[y + 1][x + 1] + datafile[y + 2][x + 2]
            s2 = datafile[y][x + 2] + datafile[y + 1][x + 1] + datafile[y + 2][x]

            p1 += s1 == "MAS" and s2 == "SAM"
            p1 += s1 == "SAM" and s2 == "SAM"
            p1 += s1 == "SAM" and s2 == "MAS"
            p1 += s1 == "MAS" and s2 == "MAS"

    print(p1)


if __name__ == "__main__":
    main()
