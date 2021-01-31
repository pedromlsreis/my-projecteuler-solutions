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
    n = 1
    while True:
        ord_n = ''.join(sorted(list(str(n))))
        a = 2 * n
        b = 3 * n
        c = 4 * n
        d = 5 * n
        e = 6 * n
        ord_a = ''.join(sorted(list(str(a))))
        ord_b = ''.join(sorted(list(str(b))))
        ord_c = ''.join(sorted(list(str(c))))
        ord_d = ''.join(sorted(list(str(d))))
        ord_e = ''.join(sorted(list(str(e))))
        if ord_n == ord_a == ord_b == ord_c == ord_d == ord_e:
            result = n
            break
        n += 1
    return result
    

print(get_composites())
# if __name__ == "__main__":
#     logger = MarkdownLogger(last_problem=723)
#     problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
#     startTime = time.time()
#     solution = run()
#     duration = round(time.time() - startTime, 5)
#     logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
#     print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")