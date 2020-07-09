## Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! 
# If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger

def run():
    with open("p067_triangle.txt", "r") as txt:
        triangle = txt.readlines()

    for line_id, line in enumerate(triangle):
        triangle[line_id] = [int(n) for n in line.split("\n")[0].split(" ")]


    for line in range(len(triangle)-2, -1, -1): 
        for pos in range(line+1):
            if triangle[line+1][pos] > triangle[line+1][pos+1]: 
                triangle[line][pos] += triangle[line+1][pos] 
            else: 
                triangle[line][pos] += triangle[line+1][pos+1] 
  
    result = triangle[0][0]
    print(f"result: {result}")
    return result

                       
if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")