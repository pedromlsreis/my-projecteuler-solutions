## Problem 206

# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import math


def run():
    form = "1_2_3_4_5_6_7_8_9_0"

    n = int(math.sqrt(int(form.replace("_", "0"))))
    s = str(n ** 2)

    while len(s) == len(form):
        s = str(n ** 2)
        if (
            s[0] == "1"
            and s[2] == "2"
            and s[4] == "3"
            and s[6] == "4"
            and s[8] == "5"
            and s[10] == "6"
            and s[12] == "7"
            and s[14] == "8"
            and s[16] == "9"
            and s[18] == "0"
        ):
            # regex pattern matching and all() with a for loop
            # with list comprehension methods were both slower
            break

        n += 1

    return n


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(
        solution, problem_id=problem_id, duration=duration, language="Python"
    )
    print(
        f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds."
    )
