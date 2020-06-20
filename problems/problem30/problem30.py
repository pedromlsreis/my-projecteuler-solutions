## Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


import time, tqdm

def run():
    power = 5
    results = 0

    # while len(results) != 3:
    for number in tqdm.tqdm(range(2, 10000000)):
        result = []
        digits = [digit for digit in str(number)]
        result = sum([int(i)**power for i in digits])
        if result == number:
            results += result
        
    print(f"result: {results}")

                       
if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"\nThe script took {round(time.time() - startTime, 2)} seconds.")