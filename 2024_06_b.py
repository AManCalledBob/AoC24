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
            starty, startx = index, row.find("^")
            break

    width = len(datafile[0])
    height = len(datafile)
    loopcount = 0

    for iy in range(height):
        for ix in range(width):
            # print(f"Checking {iy},{ix}")
            current_char = datafile[iy][ix]
            if current_char not in ("^", "#"):
                datafile[iy] = datafile[iy][:ix] + "#" + datafile[iy][ix + 1 :]

                y, x = starty, startx
                dy, dx = -1, 0
                steps = 0

                while inrange(y, x, width, height) and (steps <= width * height):
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
                        steps += 1
                    else:
                        # print(f"Finished {steps}")
                        break

                datafile[iy] = datafile[iy][:ix] + current_char + datafile[iy][ix + 1 :]

                if steps >= width * height:
                    loopcount += 1
                    print(f"Loop Found {iy},{ix}")

    print(loopcount)


if __name__ == "__main__":
    main()
