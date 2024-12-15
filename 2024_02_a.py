""" Advent of Code 2024 """

# pylint: disable=line-too-long

import os


def is_safe(numbers) -> bool:
    all_increasing = True
    all_decreasing = True
    two_adjacent = True
    for item, index in enumerate(numbers[:-1]):
        current = numbers[item]
        next = numbers[item + 1]
        all_increasing = all_increasing and (current > next)
        all_decreasing = all_decreasing and (current < next)
        max_difference = max(current - next, next - current)
        two_adjacent = two_adjacent and (1 <= max_difference <= 3)
    return (all_increasing or all_decreasing) and two_adjacent


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0]}_input_data.txt", encoding="utf-8"
    ) as input_file:
        safe_reports = 0
        for oneline in input_file.read().splitlines():
            numbers = list(map(int, oneline.split()))
            safe_reports += is_safe(numbers)
            print(f"There are {safe_reports}")


if __name__ == "__main__":
    main()
