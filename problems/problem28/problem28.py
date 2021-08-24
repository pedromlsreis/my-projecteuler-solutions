## Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import numpy as np


def create_matrix(i=5):
    matrix = np.zeros((i, i))
    c = int(np.round(i / 2))

    n_moves = []
    for x in range(i):
        n_moves.append(x + 1)
        n_moves.append(x + 1)

    prev_pos = [c, c]
    matrix[tuple(prev_pos)] = 1
    val = 2

    pos = ["right", "down", "left", "up"]
    x = 0

    for moves in n_moves:
        if x == 4:
            x -= 4

        direction = pos[x]
        for move in range(moves):
            if np.all(matrix):
                break

            if direction == "right":
                prev_pos[1] += 1

            elif direction == "down":
                prev_pos[0] += 1

            elif direction == "left":
                prev_pos[1] -= 1

            elif direction == "up":
                prev_pos[0] -= 1

            matrix[tuple(prev_pos)] = val
            val += 1

        x += 1
    return matrix


def run(n=1001):
    matrix = create_matrix(n)
    c = int(np.round(n / 2))
    result = 0

    for i, line in enumerate(matrix[::-1]):
        result += line[i]

    result = np.trace(matrix) + np.trace(matrix[::-1]) - matrix[(c, c)]
    return int(result)


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(
        solution, problem_id=problem_id, duration=duration, language="Python"
    )
    print(solution)
    print(f"\nThe script took {round(duration, 2)} seconds.")
