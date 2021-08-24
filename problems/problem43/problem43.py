## Problem 43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import itertools


def is_pandigital(number):
    min_d, max_d = 0, 9
    nr_list = sorted(list(str(number)))
    return nr_list == list(range(min_d, max_d + 1))


def is_ss_divisible(number):
    divs = [2, 3, 5, 7, 11, 13, 17]
    n_div = 0
    while n_div < len(divs):
        div = divs[n_div]
        if int(str(number)[n_div + 1 : n_div + 4]) % div != 0:
            return False
        n_div += 1
    return True


def run():
    min_d, max_d = 0, 9
    result = 0
    numbers = list(itertools.permutations(list(range(min_d, max_d + 1))))
    for n in numbers:
        number = int("".join([str(digit) for digit in n]))
        if len(str(number)) == 10:
            if is_ss_divisible(number):
                result += number
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
