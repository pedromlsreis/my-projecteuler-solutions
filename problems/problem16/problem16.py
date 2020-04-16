# # Problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

import time
import math


def run():
    solution = 0
    num = 2
    power = 1000

    power_sum = num ** power
    print(f"{num}**{power}={power_sum}")
    
    for i in str(power_sum):
        solution += int(i)
    
    print("solution:", solution)

                       
if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"\nThe script took {round(time.time() - startTime, 2)} seconds.")