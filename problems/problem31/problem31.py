## Problem 31
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any coins?

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import numpy as np, pandas as pd

def run():
    cap = 200
    b = 100
    c = 50
    d = 20
    e = 10
    f = 5
    g = 2
    h = 1

    result = 1 # 2£ case

    # 100p coins
    for n_b in range(int(cap/b) + 1):
        # 50p coins
        for n_c in range(int((cap - n_b*b) / c) + 1):
            # 20p coins
            for n_d in range(int((cap - n_b*b - n_c*c) / d) + 1):
                # 10p coins
                for n_e in range(int((cap - n_b*b - n_c*c - n_d*d) / e) + 1):
                    # 5p coins
                    for n_f in range(int((cap - n_b*b - n_c*c - n_d*d - n_e*e) / f) + 1):
                        # 2p coins
                        for n_g in range(int((cap - n_b*b - n_c*c - n_d*d - n_e*e - n_f*f) / g) + 1):
                            # 1p coins
                            for n_h in range(int((cap - n_b*b - n_c*c - n_d*d - n_e*e - n_f*f - n_g*g) / h) + 1):
                                if n_b*b + n_c*c + n_d*d + n_e*e + n_f*f + n_g*g + n_h*h == cap:
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