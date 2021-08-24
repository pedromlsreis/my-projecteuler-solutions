## Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import time
import string
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def run():
    filename = "p022_names.txt"
    with open(filename) as textfile:
        names = textfile.readline()

    names = sorted(
        name for name in names.upper().replace('"', "").replace(r"\n", "").split(",")
    )

    result = 0
    for pos, name in enumerate(names):
        for n, letter in enumerate(string.ascii_uppercase):
            name = name.replace(letter, str(n + 1) + " ")
        result += sum([int(number) for number in name.split(" ")[:-1]]) * (pos + 1)

    print(f"result: {result}")
    return result


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
