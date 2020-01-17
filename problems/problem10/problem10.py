# # Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


import time

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


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")