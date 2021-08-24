## Problem 36
# The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def run():
    result = 0
    for number in range(0, 1000000):
        if str(number) == str(number)[::-1]:
            if bin(number)[2:] == bin(number)[-1:1:-1]:
                result += number
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
    print(
        f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds."
    )
