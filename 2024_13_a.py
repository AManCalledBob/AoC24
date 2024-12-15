""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import re
from sympy import symbols, Eq, solve


def calc_cost(ax, ay, bx, by, px, py) -> int:

    x, y = symbols("x y", integer=True)
    eq1 = Eq(ax * x + bx * y, px)
    eq2 = Eq(ay * x + by * y, py)
    solutions = solve(
        (
            eq1,
            eq2,
        ),
        (x, y),
        dict=True,
    )

    if solutions:
        result = 3 * solutions[0][x] + solutions[0][y]
    else:
        result = 0

    return result


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = str(input_file.read())

    subtotal = 0
    for eachmachine in datafile.split("\n\n"):
        regex = r"Button \w: X\+(\d+), Y\+(\d+)\nButton \w: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
        ax, ay, bx, by, x, y = [int(v) for v in re.findall(regex, eachmachine)[0]]
        subtotal += calc_cost(ax, ay, bx, by, x, y)
    print(subtotal)


if __name__ == "__main__":
    main()
