""" Advent of Code 2024 """

# pylint: disable=line-too-long
import os
import numpy as np
import random
from queue import Queue


corrupted = list()


def find_path(maze):
    # BFS algorithm to find the shortest path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    end = (maze.shape[0] - 1, maze.shape[1] - 1)
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

    for item in datafile:
        x, y = list(map(int, item.split(",")))
        corrupted.append((y, x))

    gridsize = 71
    for total in range(1024, len(corrupted)):

        index = 0
        maze = []
        for i in range(gridsize):
            line = []
            for j in range(gridsize):
                if (i, j) in corrupted and corrupted.index((i, j)) <= total:
                    line.append("#")
                    index += 1
                else:
                    line.append(".")
            maze.append(line)
        mymaze = np.array(maze)

        print(f"Checking a level {total}")
        pathlength = find_path(mymaze)
        if pathlength == None:
            print(f"Failed at {corrupted[total]}")
            break

    # print(f"Length of path is {len(pathlength)}")


if __name__ == "__main__":
    main()
