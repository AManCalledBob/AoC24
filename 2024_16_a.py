""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import operator
import matplotlib.pyplot as plt
import numpy as np
from collections import deque


def draw_maze(maze):
    maze_array = np.array(maze)
    plt.imshow(maze_array, cmap="binary")
    plt.xticks([]), plt.yticks([])  # Hide the axes ticks
    plt.show()


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


def calc_cost(thepath: list, pos: tuple) -> int:
    total = 0
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dir = 2
    for nextloc in thepath:
        print(pos, nextloc)
        differance = tuple(map(operator.sub, nextloc, pos))
        if differance in directions:
            newdir = directions.index(differance)
            if newdir == dir:
                total += 1
            else:
                total += 1000
                dir = newdir
        pos = nextloc
    return total


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    maze = []

    for y, oneline in enumerate(datafile):
        currentline = []
        for x, onechar in enumerate(oneline):
            match onechar:
                case "#":
                    currentline.append(1)
                case ".":
                    currentline.append(0)
                case "S":
                    currentline.append(0)
                    start_point = (y, x)
                case "E":
                    currentline.append(0)
                    end_point = (y, x)
        maze.append(currentline)

    # draw_maze(maze)

    path = bfs(maze, start_point, end_point)
    print(f"The route cost is {calc_cost(path, start_point)}")


# https://sqlpad.io/tutorial/python-maze-solver/


if __name__ == "__main__":
    main()
