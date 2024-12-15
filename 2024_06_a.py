""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os


def inrange(y: int, x: int, maxy: int, maxx: int) -> bool:
    return x >= 0 and y >= 0 and x < maxx and y < maxy


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0]}_input_data.txt", encoding="utf-8"
    ) as input_file:
        datafile = input_file.read().splitlines()

    for index, row in enumerate(datafile):
        if "^" in row:
            y, x = index, row.find("^")
            break

    dy, dx = -1, 0
    visited_locations = set()

    while inrange(y, x, len(datafile[0]), len(datafile)):

        if inrange(y + dy, x + dx, len(datafile[0]), len(datafile)):
            if datafile[y + dy][x + dx] == "#":
                # print(f"{y},{x} Rotate")
                match (dy, dx):
                    case (-1, 0):
                        dy, dx = 0, 1
                    case (0, 1):
                        dy, dx = 1, 0
                    case (1, 0):
                        dy, dx = 0, -1
                    case (0, -1):
                        dy, dx = -1, 0
            x += dx
            y += dy
            visited_locations.add((y, x))
        else:
            print(f"Finished {len(visited_locations)}")
            break


if __name__ == "__main__":
    main()
