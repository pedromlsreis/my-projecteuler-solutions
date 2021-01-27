## Problem 52

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger


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
    

if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")