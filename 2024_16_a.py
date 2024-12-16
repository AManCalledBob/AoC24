""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import operator

from collections import deque


def bfs(maze, start, end):
    queue = deque([start])  # Create a queue and add the start position
    paths = {start: None}  # Keep track of paths
    width, height = len(maze[0]), len(maze)

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()
        if current == end:
            break

        for direction in directions:
            nx, ny = current[0] + direction[0], current[1] + direction[1]
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] == 0 and (nx, ny) not in paths:
                queue.append((nx, ny))
                paths[(nx, ny)] = current  # Track the path

    # Reconstruct the path from end to start
    path = []
    while end is not None:
        path.insert(0, end)
        end = paths[end]
    return path


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()


# https://sqlpad.io/tutorial/python-maze-solver/


if __name__ == "__main__":
    main()
