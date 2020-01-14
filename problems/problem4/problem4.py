# # Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


import time

def run():
    palindromes = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            result = i*j
            if str(result)[:3] == str(result)[3::][::-1]:
                palindromes.append(result)

    largest_palindrome = max(palindromes)
    print("Answer:", largest_palindrome)


if __name__ == "__main__":
    startTime = time.time()
    run()
    print (f"\nThe script took {round(time.time() - startTime, 2)} seconds.")