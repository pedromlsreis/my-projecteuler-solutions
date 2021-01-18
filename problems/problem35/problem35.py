## Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


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


def is_circular(prime_number):
    n_str = str(prime_number)
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:] + n_str[:i])):
            return False
    return True


def run():
    n = 100
    result = 13
    while n < 1000000:
        if is_prime(n):
            if is_circular(n):
                result += 1
                
        n += 1
    return result


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")