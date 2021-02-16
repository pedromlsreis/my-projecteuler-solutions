## Problem 55

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
# Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
# In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one,
# with all the computing power that exists, has managed so far to map it to a palindrome.
# In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?


import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import math


def check_palindrome(s):
    return str(s) == str(s)[::-1]


def rev_and_add(n):
    return n + int(str(n)[::-1])


def run():
    result = 0
    n = 1
    max_n = 10000 - n
    
    while n <= max_n:
        iters = 1
        while iters < 50:
            if iters == 1:
                r = rev_and_add(n)
            else:
                r = rev_and_add(r)
            
            if check_palindrome(r):
                result += 1
                break

            iters += 1

        n += 1
    return max_n - result


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")