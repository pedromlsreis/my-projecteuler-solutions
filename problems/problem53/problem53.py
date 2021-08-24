## Problem 53

# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, (5 3) = 10.

# In general, (n r) = n! / (r! * (n - r)!), where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.

# It is not until n=23, that a value exceeds one-million: (23 10) = 11440066.

# How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import math


def calc_combs(n, r):
    if 0 <= r <= n:
        return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    else:
        raise ValueError("In (n r) notation, 0 <= r <= n.")


def run():
    result = 0
    n = 1
    while 1 <= n <= 100:
        r = 1
        while r <= n:
            if calc_combs(n, r) > 1_000_000:
                result += 1
            r += 1
        n += 1

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
