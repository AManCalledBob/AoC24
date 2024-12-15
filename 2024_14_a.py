""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import re


def printgrid(drawwidth: int, drawheight: int, datapoints: tuple):
    print(datapoints)

    for y in range(drawheight):
        for x in range(drawwidth):
            if [x, y] in datapoints:
                print(datapoints.count([x, y]), end="")
            else:
                print(".", end="")
        print()
    print()


def countinrange(x, y, p, q, datapoints):

    print(f"Counting from {x,y} to {p,q}")
    total = 0
    for robot in datapoints:
        total += x <= robot[0] <= p and y <= robot[1] <= q
    return total


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    fullhight = 103
    fullwidth = 101
    seconds = 100

    robots = []
    total = 0

    for eachmachine in datafile:
        regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
        px, py, vx, vy = [int(v) for v in re.findall(regex, eachmachine)[0]]

        # for seconds in range(6):
        newx = (px + (vx * seconds)) % fullwidth
        newy = (py + (vy * seconds)) % fullhight
        robots.append([newx, newy])
    printgrid(fullwidth, fullhight, robots)

    halfwidth = fullwidth // 2
    halfheight = fullhight // 2
    total = countinrange(0, 0, halfwidth - 1, halfheight - 1, robots)
    total *= countinrange(halfwidth + 1, 0, fullwidth, halfheight - 1, robots)
    total *= countinrange(0, halfheight + 1, halfwidth - 1, fullhight, robots)
    total *= countinrange(halfwidth + 1, halfheight + 1, fullwidth, fullhight, robots)
    print(total)


if __name__ == "__main__":
    main()
