## Problem 42

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger
import string


def convert_letter(letter):
    if str(letter).lower() in string.ascii_lowercase:
        return list(string.ascii_lowercase).index(str(letter).lower()) + 1
    else:
        return 0


def is_triangle_word(word):
    score = 0
    for l in word:
        score += convert_letter(l)

    tri = [(i / 2) * (i + 1) for i in range(0, 100)]
    return score in tri


def run():
    result = 0
    with open("p042_words.txt", "r") as f:
        file = f.read()
    
    words = file.split('","')
    for word in words:
        if is_triangle_word(word):
            result += 1
    
    return result


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe solution is {solution} and the script took {round(duration, 2)} seconds.")