# # Problem 6

# The sum of the squares of the first ten natural numbers is,

# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import time

def run():
    import math

    sum1 = 0
    sum2 = 0

    for i in range(1, 101):
        sum1 += (i ** 2)
        sum2 += i
    
    sum2 = sum2 ** 2
    diff = sum2 - sum1

    print("Answer:", diff)


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")