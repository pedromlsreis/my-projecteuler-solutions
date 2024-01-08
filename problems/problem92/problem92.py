## Problem 92

# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?


import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def split_and_add_squares(n):
    return sum(int(x) ** 2 for x in str(n))

def run():
    result = 0

    for num in range(1, 10000000):
        chain = set()
        next = num

        while next != 1 and next != 89 and next not in chain:
            chain.add(next)
            next = split_and_add_squares(next)

        if next == 89:
            result += 1

    return result


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(
        f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds."
    )
