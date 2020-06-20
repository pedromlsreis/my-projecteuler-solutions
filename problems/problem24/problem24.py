## Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


import time, itertools, numpy as np

def run():
    result = int("".join(str(char) for char in list([perm for index, perm in enumerate(itertools.permutations(np.arange(0, 10))) if index==1000000-1][0])))
    print(f"result: {result}")

                       
if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"\nThe script took {round(time.time() - startTime, 2)} seconds.")