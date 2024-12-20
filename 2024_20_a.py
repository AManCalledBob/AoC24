""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import numpy as np
import random
from queue import Queue
from itertools import combinations


corrupted = list()


def find_path(maze, start, end):
    # BFS algorithm to find the shortest path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # start = (0, 0)
    # end = (maze.shape[0] - 1, maze.shape[1] - 1)
    visited = np.zeros_like(maze, dtype=bool)
    visited[start] = True
    queue = Queue()
    queue.put((start, []))
    while not queue.empty():
        (node, path) = queue.get()
        for dx, dy in directions:
            next_node = (node[0] + dx, node[1] + dy)
            if next_node == end:
                return path + [next_node]
            if (
                0 <= next_node[0] < maze.shape[0]
                and 0 <= next_node[1] < maze.shape[1]
                and maze[next_node] == "."
                and not visited[next_node]
            ):
                visited[next_node] = True
                queue.put((next_node, path + [next_node]))
    return None


def main():
    """Main Function"""

    with open(
        f"{os.path.basename(__file__).split('.')[0][:-2]}_input_data.txt",
        encoding="utf-8",
    ) as input_file:
        datafile = input_file.read().splitlines()

    blocklist = []

    maze = []
    height = len(datafile)
    width = len(datafile[0])

    for y, yval in enumerate(datafile):
        oneline = []
        for x, xval in enumerate(yval):
            match xval:
                case "#":
                    oneline.append("#")
                    if 0 < x < width and 0 < y < height:
                        blocklist.append((y, x))
                case "S":
                    start = (y, x)
                    oneline.append(".")
                case "E":
                    end = (y, x)
                    oneline.append(".")
                case _:
                    oneline.append(".")
        maze.append(oneline)
    mymaze = np.array(maze)
    baseline = len(find_path(mymaze, start, end))
    print(f"Baseline is {baseline} picoseconds")

    scoreboard = [0] * (baseline + 1)

    for cheats in combinations(blocklist, 1):
        # for cheats in blocklist:
        print(f"Checking {cheats}")
        mymaze[cheats[0]] = "."
        # mymaze[cheats[1]] = "."
        current = len(find_path(mymaze, start, end))
        scoreboard[current] += 1
        mymaze[cheats[0]] = "#"
        # mymaze[cheats[1]] = "#"

    for index, item in enumerate(list(reversed(scoreboard))):
        if item > 0 and index > 0:
            print(f"There are {item} cheats that save {index} picoseconds")


if __name__ == "__main__":
    main()
