""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
from itertools import combinations, zip_longest

operators = ["+", "*", "|"]


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    total = 0
    for eachline in datafile:
        answer, testvalues = eachline.split(":")
        answer = int(answer)
        testvalues = list(map(int, testvalues.split()))

        newops = list(operators * (len(testvalues) - 1))
        for testsum in combinations(newops, (len(testvalues) - 1)):
            # print(answer, testvalues, testsum)
            subtotal = testvalues[0]
            for index, item in enumerate(testvalues[1:]):
                match testsum[index]:
                    case "+":
                        subtotal += item
                    case "*":
                        subtotal *= item
                    case "|":
                        subtotal = int(str(subtotal) + str(item))
                if subtotal > answer:
                    break
            if subtotal == answer:
                print(f"{answer}, {testvalues}, {testsum} is valid")
                total += answer
                break
    print(total)


if __name__ == "__main__":
    main()
