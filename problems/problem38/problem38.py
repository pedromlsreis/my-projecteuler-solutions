## Problem 38

# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import itertools


def is_pandigital(number):
    pandigital = 123456789
    if int(''.join(sorted(list(str(number))))) == pandigital:
        return True
    else:
        return False


def run():
    result = 0
    n = 1
    
    s = ""

    while n < 10000:
        print(f"Testing number {n}...")
        test = set([])

        s = ""
        for m in range(1, 9 - len(str(n)) + 1):
            s += str(n * m)
            if len(s) > len("123456789"):
                break
            elif len(s) == len("123456789"):
                test.add(s)
        
        for t in test:
            print(f"\tTrying {t}...")
            if is_pandigital(t):
                if int(t) > result:
                    result = int(t)
                    print(f"result updated: {result}")

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