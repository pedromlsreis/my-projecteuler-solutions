## Problem 40

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger


def run():
    digits = "."
    n = 1
    
    while len(digits) < 1000001:
        digits += str(n)
        n += 1
            
    return int(digits[1]) * int(digits[10]) * int(digits[100]) * int(digits[1000]) * int(digits[10000]) * int(digits[100000]) * int(digits[1000000])


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")