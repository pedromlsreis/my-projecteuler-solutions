# # Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import time

def run():
    # TODO: taking 5min to run. Turn this to 1min.
    x = 20

    while True:        
        no_remainders = True
        
        for i in range(2,21):
            if x % i != 0:
                no_remainders = False
        
        if no_remainders:
            smallest_answer = x
            break
        
        x += 1
    
    print("Answer:", smallest_answer)


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")