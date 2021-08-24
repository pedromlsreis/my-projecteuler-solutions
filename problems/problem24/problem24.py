## Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


import itertools
import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import numpy as np


def run():
    result = int(
        "".join(
            str(char)
            for char in list(
                [
                    perm
                    for index, perm in enumerate(
                        itertools.permutations(np.arange(0, 10))
                    )
                    if index == 1000000 - 1
                ][0]
            )
        )
    )
    print(f"result: {result}")
    return result


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(
        solution, problem_id=problem_id, duration=duration, language="Python"
    )
    print(f"\nThe script took {round(duration, 2)} seconds.")
