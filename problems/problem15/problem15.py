# # Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

import math
import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger

def run():
    """
    Problema de combinatória. Percorrer matriz de 20x20 implica na mesma percorrer 20 posições
    em x e 20 em y. Resta é saber qual a sua posição.
    """
    last = 20
    # for n in range(1, last+1):
    #     solution = int(math.factorial(2 * n) / (math.factorial(n) * math.factorial(n)))
    #     print(f"{n}x{n}: {solution}")
    
    # print(f"final solution: {solution}")
    return int(math.factorial(2 * last) / (math.factorial(last) * math.factorial(last)))


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")