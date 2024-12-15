""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
from itertools import combinations
from functools import cmp_to_key

rules = set()
produce = []


cmp = cmp_to_key(lambda x, y: 1 - 2 * (str(x) + "|" + str(y) in rules))


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0]}_input_data.txt", encoding="utf-8"
    ) as input_file:
        for oneline in input_file.read().splitlines():
            if "|" in oneline:
                rules.add(oneline)
            elif "," in oneline:
                results = list(map(int, oneline.split(",")))
                produce.append(results)

    running_total = 0
    for index, current in enumerate(produce):
        isvalid = check_isvalid(current)
        if not isvalid:
            totest = sorted(current, key=cmp)
            running_total += totest[len(totest) // 2]
    print(f"{running_total}")


def check_isvalid(current):
    isvalid = True
    for left, right in combinations(current, 2):
        isvalid = isvalid and (str(left) + "|" + str(right) in rules)
    return isvalid


if __name__ == "__main__":
    main()
