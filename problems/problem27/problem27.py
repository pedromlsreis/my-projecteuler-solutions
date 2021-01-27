## Problem 27

# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000 where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import math


def is_prime(number):
    if number == 1 or number < 0:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def run():
    result = [0, 0, 0]
    max_mod_a = 999
    max_mod_b = 1000
    for a in range(- max_mod_a, max_mod_a + 1):
        for b in range(- max_mod_b, max_mod_b + 1):
            n = 0
            while is_prime(int(n**2 + a * n + b)):
                n += 1
            if n - 1 > result[2]:
                result = [a, b, n - 1]

    return result[0] * result[1]
    

if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")