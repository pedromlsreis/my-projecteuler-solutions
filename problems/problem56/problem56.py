## Problem 56
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger

def run():
    maxSum = 0

    for a in range(0, 101):
        for b in range(0, 101):
            if sum([int(n) for n in str(a**b)]) > maxSum:
                maxSum = sum([int(n) for n in str(a**b)])

    print(f"result: {maxSum}")
    return maxSum

                       
if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")