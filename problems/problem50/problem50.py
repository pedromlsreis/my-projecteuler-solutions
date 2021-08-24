## Problem 50

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import math


def is_prime(nr):
    if nr <= 1:
        return False
    for i in range(2, int(math.sqrt(nr) + 1)):
        if nr % i == 0:
            return False
    return True


def run():
    result = 0
    n = 2
    first_n_primes = [0]
    while first_n_primes[-1] < 1000000:
        if is_prime(n):
            first_n_primes.append(n)
        n += 1

    for j, i in enumerate(first_n_primes):
        if result + i >= 1000000:
            last_index = j
            break
        result += i

    x = 0
    while is_prime(result) == False:
        result -= first_n_primes[last_index - x - 1]

    return result


print(run())
# if __name__ == "__main__":
#     logger = MarkdownLogger(last_problem=723)
#     problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
#     startTime = time.time()
#     solution = run()
#     duration = round(time.time() - startTime, 5)
#     logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
#     print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")
