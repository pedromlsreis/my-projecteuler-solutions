## Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import operator
from fractions import Fraction


def is_non_trivial(numerator, denominator):
    if numerator % 10 == 0 or denominator % 10 == 0 or denominator == 0:
        return False

    n = str(numerator)
    d = str(denominator)

    if n[0] == d[0] and int(d[1]) != 0:
        return int(n[1]) / int(d[1]) == numerator / denominator
    elif n[0] == d[1] and int(d[0]) != 0:
        return int(n[1]) / int(d[0]) == numerator / denominator
    elif n[1] == d[0] and int(d[1]) != 0:
        return int(n[0]) / int(d[1]) == numerator / denominator
    elif n[1] == d[1] and int(d[0]) != 0:
        return int(n[0]) / int(d[0]) == numerator / denominator
    else:
        return False

def run():
    four_fracs = [Fraction(49, 98)]
    n = 10
    d = 11

    b, n_batches = 0, 0

    while len(four_fracs) < 4:
        if b == 500:  # batch size: 500
            b = 0
            n += 1  # atualizar numerador quando batch é atingido
            n_batches += 1
            d = 11 + n_batches  # starting point do denominador

        if is_non_trivial(n, d):
            if n != 49 or d != 98:
                four_fracs.append(Fraction(n, d))

        b += 1
        d += 1  # denominador sempre a crescer

    return (four_fracs[0] * four_fracs[1] * four_fracs[2] * four_fracs[3]).denominator


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")
