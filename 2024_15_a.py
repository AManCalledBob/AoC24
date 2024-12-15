""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import operator


def display_grid(py, px, my, mx: int, block: list, boxes: list, move: str) -> None:
    print(f"Move {move}:")
    for y in range(my):
        for x in range(mx):
            toprint = "."
            if (y, x) in block:
                toprint = "#"
            if (y, x) in boxes:
                toprint = "O"
            if (y, x) == (py, px):
                toprint = "@"
            print(toprint, end="")
        print()
    print()


def domove(myobj, delta, myblocks, myboxes):
    print(f"Do move called with {myobj}, {delta}")

    newpos = tuple(map(operator.add, myobj, delta))
    if newpos in myblocks:
        print("Block")
        return myobj, myboxes
    elif newpos in myboxes:
        print("Boxes")
        newmyobj, newmyboxes = domove(newpos, delta, myblocks, myboxes)
        newmyboxes.append(newmyobj)
        newmyboxes.remove(newpos)
        return newpos, myboxes
    else:
        print("Can Move")
        return newpos, myboxes


def calcgps(boxes: list) -> int:
    print("Calc GPS called with warehouse looking like")
    total = 0
    for _, item in enumerate(boxes):
        total += item[0] * 100 + item[1]
    return total


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    moveset = ""
    blocks = []
    boxes = []
    maxy, maxx = 0, len(datafile[0])

    for iy, yline in enumerate(datafile):
        if "#" in yline:
            maxy += 1
            for ix, xchar in enumerate(yline):
                if xchar == "@":
                    y, x = iy, ix
                if xchar == "#":
                    blocks.append((iy, ix))
                if xchar == "O":
                    boxes.append((iy, ix))
        else:
            moveset = moveset + yline
    display_grid(y, x, maxy, maxx, blocks, boxes, "Initial")

    for _, onemove in enumerate(moveset):
        display_grid(y, x, maxy, maxx, blocks, boxes, onemove)
        match onemove:
            case "<":
                (y, x), boxes = domove((y, x), (+0, -1), blocks, boxes)
            case ">":
                (y, x), boxes = domove((y, x), (+0, +1), blocks, boxes)
            case "^":
                (y, x), boxes = domove((y, x), (-1, +0), blocks, boxes)
            case ">":
                (y, x), boxes = domove((y, x), (+1, +0), blocks, boxes)

    print(calcgps(boxes))


if __name__ == "__main__":
    main()
