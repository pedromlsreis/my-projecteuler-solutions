# # Problem 12

# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

import math
import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger

def run():
    max_divisors = 500
    n = max_divisors
    answer = False

    while not answer:
        triangle = int((n * (n + 1)) / 2)
        print(f"Testing {triangle}...")
        
        divisor_counter = 0

        if triangle % 2 == 0:
            i = 1
            while not answer:
                if i == math.ceil(triangle/2) + 1:
                    break
                
                if triangle % i == 0:
                    divisor_counter += 1
                    if divisor_counter == max_divisors:
                        answer = triangle
                i += 1

        n += 1

    print("Answer:", answer)
    return answer


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")