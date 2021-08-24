## Problem 49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

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
    result = ""
    n = 1000
    flag = True
    while n < 10000 and flag:
        if is_prime(n) and n != 1487:
            all_perms = [
                int("".join(p)) for p in list(itertools.permutations(list(str(n))))
            ]
            true_perms = sorted(list(set(all_perms) - set([n])))
            for x in true_perms:
                if is_prime(x) and len(str(int(x))) == 4:
                    delta = x - n
                    if is_prime(x + delta) and len(str(int(x + delta))) == 4:
                        if x + delta in true_perms:
                            for res in sorted([n, x, x + delta]):
                                result += str(res)
                                flag = False
        n += 1
    return int(result)


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
