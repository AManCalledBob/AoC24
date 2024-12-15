""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
from itertools import combinations
from collections import defaultdict
from math import sqrt


def inbounds(y: int, x: int, my: int, mx: int) -> bool:
    return (0 <= y < my) and (0 <= x < mx)


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    # Build the nodelist
    antennas = defaultdict(list)
    antinodes = set()
    maxy, maxx = len(datafile), len(datafile[0])

    for y, yval in enumerate(datafile):
        for x, xval in enumerate(yval):
            if xval != ".":
                antennas[xval].append((y, x))

    for frequency in antennas:
        for (y1, x1), (y2, x2) in combinations(antennas[frequency], 2):
            print(f"Testing {(y1, x1), (y2, x2)}")

            # if y1 > y2:
            #     (y2, x2), (y1, x1) = (y1, x1), (y2, x2)
            # if x1 > x2:
            #     (y2, x2), (y1, x1) = (y1, x1), (y2, x2)
            dy = abs(y1 - y2)
            dx = abs(x1 - x2)

            if y1 < y2 and x1 < x2:
                y3, x3 = y2 + dy, x2 + dx
                y4, x4 = y1 - dy, x1 - dx
            elif y1 < y2 and x1 > x2:
                y3, x3 = y2 - dy, x2 + dx
                y4, x4 = y1 + dy, x1 - dx
            elif y1 > y2 and x1 > x2:
                y3, x3 = y2 - dy, x2 - dx
                y4, x4 = y1 + dy, x1 + dx
            elif y1 < y2 and x1 < x2:
                y3, x3 = y1 - dy, x1 + dx
                y4, x4 = y2 + dy, x2 + dx
            else:
                y3, x3 = y1 + dy, x1 + dx
                y4, x4 = y1 - dy, x2 - dx

            if inbounds(y3, x3, maxy, maxx):
                antinodes.add((y3, x3))

            # y4 = y2 + dy
            # x4 = x2 + dx
            if inbounds(y4, x4, maxy, maxx):
                antinodes.add((y4, x4))
    print(antinodes)


if __name__ == "__main__":
    main()
