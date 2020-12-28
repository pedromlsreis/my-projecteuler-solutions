## Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import operator

def run():
    sols = {}
    max_p = 1000
    for a in range(1, max_p + 1):
        for b in range(a, max_p - a + 1):
            for h in range(b, max_p - a - b + 1):
                p = a + b + h
                if p <= max_p:
                    if a**2 + b**2 == h**2:
                        if p in sols:
                            sols[p] += 1
                        else:
                            sols[p] = 1

    result = max(sols.items(), key=operator.itemgetter(1))[0]
    return result


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")