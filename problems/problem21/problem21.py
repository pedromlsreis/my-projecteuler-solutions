## Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import numpy as np

def find_divisors(num):
    n_divisors = set([])
    for i in range(1, int(np.round(num / 2)) + 1):
        if num % i == 0:
            n_divisors.add(i)
    
    return n_divisors


def run(n=10000):
    result = 0
    divs = {}
    for num in range(1, n):
        s = sum(find_divisors(num))
        divs[num] = s

    for k in divs.keys():
        if divs[k] in divs.keys() and k != divs[k]:
            if k == divs[divs[k]]:
                result += k

    return result


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")