## Problem 26

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger


def get_decimal_part(number):
    return str(number).split(".")[1]


def get_cycle_length(decimal_part):
    cycle = decimal_part[0]
    for d in decimal_part:
        if d == decimal_part[-1]:


    return cycle_len

def run():
    result = 0
    numerator = 1
    max_denominator = 10
    for denominator in range(2, max_denominator):
        dec = get_decimal_part(numerator/denominator)
        print(dec)
        
    return result
    
# print(get_decimal_part(1/9), type(get_decimal_part(1/9)))
print(run())
# if __name__ == "__main__":
#     logger = MarkdownLogger(last_problem=723)
#     problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
#     startTime = time.time()
#     solution = run()
#     duration = round(time.time() - startTime, 5)
#     logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
#     print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")