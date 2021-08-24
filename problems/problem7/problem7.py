# # Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def run():
    prime_number = 10001
    primes = [2]
    x = 3

    while len(primes) <= prime_number:
        append = True
        for i in primes:
            if x % i == 0:
                append = False

        if append:
            primes.append(x)

        x += 2

    answer = primes[prime_number - 1]
    print("Answer:", answer)
    return answer


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
