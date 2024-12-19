""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
from math import trunc


def decodecombo(operand, rega, regb, regc):
    if operand <= 3:
        return operand
    if operand == 4:
        return rega
    if operand == 5:
        return regb
    if operand == 6:
        return regc


def main():
    """Main Function"""

    regA = 0
    regB = 0
    regC = 0

    opcode = []

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        part1, part2 = input_file.read().split("\n\n")

        for oneline in part1.splitlines():
            txtreg, value = oneline[9:].split(": ")
            value = int(value)
            match txtreg:
                case "A":
                    regA = value
                case "B":
                    regB = value
                case "C":
                    regC = value

        memory = list(map(int, part2[9:].split(",")))

        needcomma = False
        ip = 0
        while ip < len(memory):
            match memory[ip]:
                case 0:
                    regA = regA >> decodecombo(memory[ip + 1], regA, regB, regC)
                    ip += 2
                case 1:
                    regB = regB ^ memory[ip + 1]
                    ip += 2
                case 2:
                    regB = decodecombo(memory[ip + 1], regA, regB, regC) % 8
                    ip += 2
                case 3:
                    if regA == 0:
                        ip += 2
                    else:
                        ip = memory[ip + 1]
                case 4:
                    regB = regB ^ regC
                    ip += 2
                case 5:
                    outval = decodecombo(memory[ip + 1], regA, regB, regC) % 8
                    if needcomma:
                        print(",", end="")
                    else:
                        needcomma = True
                    print(outval, end="")
                    ip += 2
                case 6:
                    regB = regA >> decodecombo(memory[ip + 1], regA, regB, regC)
                    ip += 2
                case 7:
                    regC = regA >> decodecombo(memory[ip + 1], regA, regB, regC)
                    ip += 2
    print()
    print(f"Registers {regA, regB, regC}")


if __name__ == "__main__":
    main()
