## Problem 47

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import math, operator


def is_prime(nr):
    if nr == 1:
        return False
    for i in range(2, int(math.sqrt(nr) + 1)):
        if nr % i == 0:
            return False
    return True


def get_factors(number):
    factors = []
    for i in range(2, int(math.ceil(number / 2) + 1)):
        if number % i == 0:
            if is_prime(i):
                factors.append(i)
    return factors


def run():
    n = 2
    nr_factors = 4
    consecutive = 0
    while n:
        facts = get_factors(n)
        if len(facts) == nr_factors:
            consecutive += 1
            if consecutive == nr_factors:
                return n - nr_factors + 1
        else:
            consecutive = 0
        n += 1


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
