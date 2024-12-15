""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os

stones = []


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        stones = list(input_file.read().split(" "))

    print(f"Initial arrangement {stones}")

    for blink in range(25):

        newstones = []
        for index, stone in enumerate(stones):
            # Rule 1
            if stone == "0":
                newstones.append("1")
                # Rule 2
            elif (len(stone) % 2) == 0:
                first_half = int(stone[: len(stone) // 2])
                second_half = int(stone[len(stone) // 2 :])
                newstones.append(str(first_half))
                newstones.append(str(second_half))
                # Rule 3
            else:
                newstones.append(str(int(stone) * 2024))

        print(f"After {blink+1} blinks:")
        print(newstones)
        stones = newstones
    print(f"There are {len(stones)} stones")


if __name__ == "__main__":
    main()
