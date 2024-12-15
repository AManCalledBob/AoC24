""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
from itertools import combinations

rules = set()
produce = []


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0]}_input_data.txt", encoding="utf-8"
    ) as input_file:
        for oneline in input_file.read().splitlines():
            # if "|" in oneline:
            #     left, right = oneline.split("|")
            #     rules.append((left, right))
            if "|" in oneline:
                rules.add(oneline)
            elif "," in oneline:
                results = list(map(int, oneline.split(",")))
                produce.append(results)

    running_total = 0
    for index, current in enumerate(produce):
        isvalid = True
        for left, right in combinations(current, 2):
            isvalid = isvalid and (str(left) + "|" + str(right) in rules)
        if isvalid:
            running_total += current[len(current) // 2]
    print(f"{running_total}")


if __name__ == "__main__":
    main()
