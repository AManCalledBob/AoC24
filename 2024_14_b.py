""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import re


def printgrid(drawwidth: int, drawheight: int, datapoints: tuple, elapsed):
    # print(datapoints)
    os.system("cls")

    print(f"Displaying {elapsed} itteration, of {len(datapoints)} datapoints")
    for y in range(drawheight):
        currentline = ""
        for x in range(drawwidth):
            if [x, y] in datapoints:
                currentline = currentline + "#"
            else:
                currentline = currentline + "."
        print(currentline)
    print()


def checkgrid(drawwidth: int, drawheight: int, datapoints: tuple, elapsed) -> bool:
    os.system("cls")

    treefound = False

    print(f"Displaying {elapsed} itteration")
    # printgrid(drawwidth, drawheight, datapoints, elapsed)
    for y in range(drawheight):
        currentline = ""
        for x in range(drawwidth):
            if [x, y] in datapoints:
                currentline = currentline + "#"
            else:
                currentline = currentline + " "
        treefound = "#########" in currentline
        if treefound:
            break
    return treefound


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    fullhight = 103
    fullwidth = 101
    seconds = 0

    robots = []
    deltas = []
    total = 0

    for eachmachine in datafile:
        regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
        px, py, vx, vy = [int(v) for v in re.findall(regex, eachmachine)[0]]
        robots.append([px, py])
        deltas.append([vx, vy])

    found = False
    while not found:
        seconds += 1
        newrobots = []
        for index, onerobot in enumerate(robots):
            newx = (onerobot[0] + (deltas[index][0] * seconds)) % fullwidth
            newy = (onerobot[1] + (deltas[index][1] * seconds)) % fullhight
            newrobots.append([newx, newy])
        found = checkgrid(fullwidth, fullhight, newrobots, seconds)

    printgrid(fullwidth, fullhight, newrobots, seconds)
    print(f"Tree found after {seconds}s")


if __name__ == "__main__":
    main()
