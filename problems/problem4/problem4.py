# # Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def run():
    palindromes = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            result = i * j
            if str(result)[:3] == str(result)[3::][::-1]:
                palindromes.append(result)

    largest_palindrome = max(palindromes)
    print("Answer:", largest_palindrome)
    return largest_palindrome


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(
        solution, problem_id=problem_id, duration=duration, language="Python"
    )
    print(f"\nThe script took {round(duration, 2)} seconds.")
