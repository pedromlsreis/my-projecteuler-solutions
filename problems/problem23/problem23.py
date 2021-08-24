## Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import math, operator


def get_divs(number):
    divs = [1]
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divs.extend([i, int(number / i)])
    return list(set(divs))


def is_abundant(number):
    return number < sum(get_divs(number))


def run():
    can_be = set([])
    for n in range(24, 28123 + 1):
        rest = 1
        while rest < n:
            if is_abundant(rest) and is_abundant(n - rest):
                can_be.add(n)
                break
            rest += 1

    return sum(list(set(list(range(1, 28124))) - can_be))


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
