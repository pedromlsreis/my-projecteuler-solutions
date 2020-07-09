# # Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger

def run():

    primes = {2}
    max_no = 2000000

    for x in range(3, max_no, 2):
        print (f"{x}/{max_no}...")
        
        append = True
        for p in primes:
            if x % p == 0:
                append = False
    
        if append:
            primes.add(x)
    
    answer = sum(primes)
    print("Answer:", answer)
    return answer


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")