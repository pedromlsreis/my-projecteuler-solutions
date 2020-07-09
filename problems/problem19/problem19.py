## Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime
import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger

def run():
    min_date = datetime.date(1901, 1, 1)
    max_date = datetime.date(2000, 12, 31)
    delta = (max_date - min_date).days

    counter = 0
    for day in range(delta + 1):
        d = min_date + datetime.timedelta(day)
        if (d.weekday() == 6) and (d.day == 1):
            counter += 1

    print(f"result: {counter}")
    return counter

                       
if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")