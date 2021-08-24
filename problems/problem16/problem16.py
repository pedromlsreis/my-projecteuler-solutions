# # Problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def run():
    solution = 0
    num = 2
    power = 1000

    power_sum = num ** power
    print(f"{num}**{power}={power_sum}")

    for i in str(power_sum):
        solution += int(i)

    print("solution:", solution)
    return solution


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
