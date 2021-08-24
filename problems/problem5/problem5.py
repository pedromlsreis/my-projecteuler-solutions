# # Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger

from numba import jit


@jit(nopython=True)
def run():
    x = 20

    while True:
        no_remainders = True

        for i in range(2, 21):
            if x % i != 0:
                no_remainders = False

        if no_remainders:
            smallest_answer = x
            break

        x += 1

    print("Answer:", smallest_answer)
    return smallest_answer


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
