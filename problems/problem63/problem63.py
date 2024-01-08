## Problem 63

# The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def run():
    result = 0
    for power in range(1, 100):
        for base in range(1, 10):
            if len(str(base ** power)) == power:
                result += 1
                # print(base, power, base ** power)
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
