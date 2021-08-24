## Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?


import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import itertools, math


def is_prime(nr):
    if nr == 1:
        return False
    for i in range(2, int(math.sqrt(nr) + 1)):
        if nr % i == 0:
            return False
    return True


def is_pandigital(number):
    nr_list = sorted(list(str(number)))
    return nr_list == list(range(1, len(nr_list) + 1))


def run():
    n_digits = 9
    while n_digits:
        for n in sorted(list(itertools.permutations(list(range(1, n_digits + 1)))))[
            ::-1
        ]:
            if is_prime(int("".join([str(x) for x in n]))):
                return int("".join([str(x) for x in n]))
        n_digits -= 1


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
