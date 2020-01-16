# # Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


import time

def run():
    import numpy as np

    primes = np.array([2])

    for x in range(3, 2000000, 2):
        print (f"{x}/{2000000}...")
        
        append = True
        for p in primes:
            if x % p == 0:
                append = False
        if x < 2000000:
            if append:
                primes = np.append(primes, x)
        else:
            break
    
    answer = np.sum(primes)
    print("Answer:", answer)


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")