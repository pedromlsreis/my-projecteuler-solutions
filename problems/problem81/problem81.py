## Problem 81

# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

# Matrix:
#   131   673   234   103    18
#   201    96   342   965   150
#   630   803   746   422   111
#   537   699   497   121   956
#   805   732   524    37   331

# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import pandas as pd


def run():
    data = pd.read_csv("p081_matrix.txt", sep=",")
    print(data.head())
    return data


run()

# if __name__ == "__main__":
#     logger = MarkdownLogger(last_problem=723)
#     problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
#     startTime = time.time()
#     solution = run()
#     duration = round(time.time() - startTime, 5)
#     logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
#     print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")
