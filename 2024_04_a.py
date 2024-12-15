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
    for y in range(height):
        for x in range(width):
            p1 += (
                # Horizontal Left to Right
                x + 3 < width
                and datafile[y][x] == "X"
                and datafile[y][x + 1] == "M"
                and datafile[y][x + 2] == "A"
                and datafile[y][x + 3] == "S"
            )

            p1 += (
                # Horizontal Right to Left
                x + 3 < width
                and datafile[y][x] == "S"
                and datafile[y][x + 1] == "A"
                and datafile[y][x + 2] == "M"
                and datafile[y][x + 3] == "X"
            )

            p1 += (
                # Vertical Top to Bottom
                y + 3 < height
                and datafile[y][x] == "X"
                and datafile[y + 1][x] == "M"
                and datafile[y + 2][x] == "A"
                and datafile[y + 3][x] == "S"
            )
            p1 += (
                # Down Right
                y + 3 < height
                and x + 3 < width
                and datafile[y][x] == "X"
                and datafile[y + 1][x + 1] == "M"
                and datafile[y + 2][x + 2] == "A"
                and datafile[y + 3][x + 3] == "S"
            )

            p1 += (
                # Vertical Bottom to Top
                y + 3 < height
                and datafile[y][x] == "S"
                and datafile[y + 1][x] == "A"
                and datafile[y + 2][x] == "M"
                and datafile[y + 3][x] == "X"
            )
            p1 += (
                y + 3 < height
                and x + 3 < width
                and datafile[y][x] == "S"
                and datafile[y + 1][x + 1] == "A"
                and datafile[y + 2][x + 2] == "M"
                and datafile[y + 3][x + 3] == "X"
            )
            p1 += (
                y - 3 >= 0
                and x + 3 < width
                and datafile[y][x] == "S"
                and datafile[y - 1][x + 1] == "A"
                and datafile[y - 2][x + 2] == "M"
                and datafile[y - 3][x + 3] == "X"
            )

            p1 += (
                y - 3 >= 0
                and x + 3 < width
                and datafile[y][x] == "X"
                and datafile[y - 1][x + 1] == "M"
                and datafile[y - 2][x + 2] == "A"
                and datafile[y - 3][x + 3] == "S"
            )

    print(p1)


if __name__ == "__main__":
    main()
