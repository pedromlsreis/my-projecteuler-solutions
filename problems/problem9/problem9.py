# # Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import time
import math

def run():
    # TODO: Took 2 min. Reduce time.
    total = 1000

    for a in range(1, total+1):
        for b in range(a+1, total+1):
            for c in range(b+1, total+1):
                if a**2 + b**2 == c**2:
                    if a + b + c == total:
                        answer = a * b * c
                        break                    

    print("Answer:", answer)


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")