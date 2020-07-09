## Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import tqdm

def run():
    power = 5
    maxdigits = 7
    results = 0

    for number in tqdm.tqdm(range(2, maxdigits * 9 ** power)):
        sum_ = 0
        for i in str(number):
            sum_ += int(i)**power
        if number == sum_:
            results += number
        
    print(f"result: {results}")
    return results

                       
if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")