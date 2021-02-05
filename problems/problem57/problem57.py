## Problem 57

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# By expanding this for the first four iterations, we get:
# The next three expansions are 
# , , and , but the eighth expansion, , is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?



import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import math
from fractions import Fraction


def run():
    result = 0
    n_expansions = 1000
    prev = Fraction(1 / 2)
    den = 2 + prev
    # first 3 expansions don't respect the rule so we're skipping them
    for x in range(3, n_expansions + 1):
        den = den - prev + Fraction(1 / (2 + prev))
        prev = Fraction(1 / (2 + prev))
        frac = Fraction(1 + 1 / den)
        if len(str(frac.numerator)) > len(str(frac.denominator)):
            result += 1

    return result
    

if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")