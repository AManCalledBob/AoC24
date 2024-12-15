""" Advent of Code 2024 """

# pylint: disable=line-too-long

import os

searchstring = "XMAS"


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0]}_input_data.txt", encoding="utf-8"
    ) as input_file:
        datafile = input_file.read().splitlines()

    found_count = 0
    width = len(datafile[0])
    height = len(datafile)
    # for y_index, y_value in enumerate(datafile):
    #     for x_index, x_value in enumerate(datafile[y_index]):

    #         # # Horizontal
    #         # currentstring = y_value[x_index : x_index + 4]
    #         # found_count += (
    #         #     currentstring == searchstring or currentstring == searchstring[::-1]
    #         # )

    #         # # Vertical
    #         # currentstring = (
    #         #     datafile[y_index][x_index]
    #         #     + datafile[min(y_index + 1, height - 1)][x_index]
    #         #     + datafile[min(y_index + 2, height - 1)][x_index]
    #         #     + datafile[min(y_index + 3, height - 1)][x_index]
    #         # )
    #         # found_count += (
    #         #     currentstring == searchstring or currentstring == searchstring[::-1]
    #         # )

    #         # Diag Left to Right
    #         currentstring = (
    #             datafile[y_index][x_index]
    #             + datafile[min(y_index + 1, height - 1)][min(y_index + 1, width - 1)]
    #             + datafile[min(y_index + 2, height - 1)][min(y_index + 2, width - 1)]
    #             + datafile[min(y_index + 3, height - 1)][min(y_index + 3, width - 1)]
    #         )
    #         found_count += (
    #             (currentstring == searchstring)
    #             or (currentstring == searchstring[::-1])
    #             and (y_index < 7)
    #         )

    # # Diag Right to Left
    # currentstring = (
    #     datafile[y_index][x_index]
    #     + datafile[min(y_index + 1, height - 1)][max(y_index - 1, 0)]
    #     + datafile[min(y_index + 2, height - 1)][max(y_index - 2, 0)]
    #     + datafile[min(y_index + 3, height - 1)][max(y_index - 3, 0)]
    # )
    # found_count += (
    #     currentstring == searchstring or currentstring == searchstring[::-1]
    # )

    p1 = 0
    height = len(datafile)
    width = len(datafile[0])
    for y in range(height):
        for x in range(width):
            p1 += (
                x + 3 < width
                and datafile[y][x] == "X"
                and datafile[y][x + 1] == "M"
                and datafile[y][x + 2] == "A"
                and datafile[y][x + 3] == "S"
            )

            p1 += (
                x + 3 < width
                and datafile[y][x] == "S"
                and datafile[y][x + 1] == "A"
                and datafile[y][x + 2] == "M"
                and datafile[y][x + 3] == "X"
            )

            p1 += (
                y + 3 < height
                and datafile[y][x] == "X"
                and datafile[y + 1][x] == "M"
                and datafile[y + 2][x] == "A"
                and datafile[y + 3][x] == "S"
            )
            p1 += (
                y + 3 < height
                and x + 3 < width
                and datafile[y][x] == "X"
                and datafile[y + 1][x + 1] == "M"
                and datafile[y + 2][x + 2] == "A"
                and datafile[y + 3][x + 3] == "S"
            )

            p1 += (
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
