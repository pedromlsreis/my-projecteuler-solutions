## Problem 51

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family:
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993.

# Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import itertools, math


def is_prime(nr):
    if nr <= 1:
        return False
    for i in range(2, int(math.sqrt(nr) + 1)):
        if nr % i == 0:
            return False
    return True


def run():
    n_digits = 2
    result = []

    n = int("1" + (n_digits - 1) * "0")
    n_max = int((n_digits - 1) * "8")

    # # while n <= n_max:
    # get_max
    combs = []
    found = [
        s
        for s in range(10, n_max + 1)
        if "9" not in str(s)
        and "0" not in str(s)
        and sorted(list(set(list(str(s))))) == sorted(list(str(s)))
    ]
    # print(combs)
    for s in found:
        if int("".join(sorted(list(str(s))))) not in combs:
            combs.append(s)

    # print(found)
    print(combs)
    # TODO: rever
    #         combs.remove(int(str(s)[::-1]))
    # print(combs)

    # n += 1
    return sorted(result)[0]


run()
# if __name__ == "__main__":
#     logger = MarkdownLogger(last_problem=723)
#     problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
#     startTime = time.time()
#     solution = run()
#     duration = round(time.time() - startTime, 5)
#     logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
#     print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")
