""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os


def checksum(checkstring: str) -> int:

    total = 0
    for index, value in enumerate(checkstring):
        if value.isdigit():
            total += index * int(value)
    return total


def expand(currentstring: str) -> str:

    id = 0
    newstr = ""
    for index, value in enumerate(currentstring):
        if index % 2:
            if index < len(currentstring):
                newstr = newstr + "." * int(currentstring[index])
        else:
            newstr = newstr + str(id) * int(value)
            id += 1

    return newstr


def compress(currenstring: str) -> str:
    print(f"Compress called with ({currenstring})")
    headindex = 0
    tailindex = len(currenstring) - 1

    # while blocks_to_replace > 0:
    while headindex < tailindex:
        # print(f"{currenstring} {headindex} {tailindex} {currenstring[headindex]}")
        if currenstring[headindex] == ".":

            while currenstring[tailindex] == ".":
                tailindex -= 1

            currenstring = (
                currenstring[:headindex]
                + currenstring[tailindex]
                + currenstring[headindex + 1 :]
            )

            currenstring = (
                currenstring[:tailindex] + "." + currenstring[tailindex + 1 :]
            )
            tailindex -= 1
            # print(currenstring)
        headindex += 1
    return currenstring


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    for oneline in datafile:
        print(f"Starting with ({oneline})")
        oneline = expand(oneline)
        print(f"Expand ({oneline})")

        oneline = compress(oneline)
        print()
        print(f"{checksum(oneline)}")


if __name__ == "__main__":
    main()
