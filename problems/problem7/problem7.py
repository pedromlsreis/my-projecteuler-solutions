# # Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


import time

def run():
    prime_number = 10001
    primes = [2]
    x = 3

    while len(primes) <= prime_number:
        append = True
        for i in primes:
            if x % i == 0:
                append = False
        
        if append:
            primes.append(x)
        
        x += 2

    answer = primes[prime_number - 1]
    print("Answer:", answer)


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")