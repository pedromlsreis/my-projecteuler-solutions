# # Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import time

def run():
    import math
    
    number = 600851475143
    factors = []

    for i in range(1, int(math.sqrt(number))+1, 2): # excluding even numbers, given number is odd
        print(f"Picking the factors {i}/{int(math.sqrt(number))}...")
        if number % i == 0:
            factors.append(i)
        
    print("Done...")

    prime_factors = []
    prime_factors.append(factors[1]) # excluding 1

    for pos, n in enumerate(factors[1:]):
        print(f"Picking the prime factors {pos+1}/{len(factors)-1}...")
        append = True
        for p in prime_factors:
            if n % p == 0:
                append = False
    
        if append:
            prime_factors.append(n)
    
    print("Done...")
    largest_prime = prime_factors[-1]
    print("Answer:", largest_prime)


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")
