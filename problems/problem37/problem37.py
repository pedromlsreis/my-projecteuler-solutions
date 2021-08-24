## Problem 37

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import math, operator


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def is_truncatable(prime_number):
    n_str = str(prime_number)
    for pos in range(1, len(n_str)):
        if not is_prime(int(n_str[pos:])) or not is_prime(int(n_str[:pos])):
            return False
    return True


def run():
    n = 8
    result = 0
    qtt = 0
    while qtt < 11:
        if is_prime(n):
            if is_truncatable(n):
                qtt += 1
                result += n

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
