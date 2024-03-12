"""
Mix
"""

import time

"""

Fibonacci sequence
Up to 15th position
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

F(n) = F(n-1) + F(n-2)
"""


def fibonacci_of(n):
    # base case
    if n in [0, 1]:
        return n

    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


#
# tic = time.perf_counter()
# print([fibonacci_of(n) for n in range(40)])
# toc = time.perf_counter()
# print(f"fibo1 time: {toc - tic:0.4f}s")

# Improvement with memoization
cache = {0: 0, 1: 1}


def fibonacci_mem_of(n):
    if n in cache:
        return cache[n]

    cache[n] = fibonacci_mem_of(n - 1) + fibonacci_mem_of(n - 2)
    return cache[n]


#
# tic = time.perf_counter()
# print([fibonacci_of(n) for n in range(40)])
# toc = time.perf_counter()
# print(f"fibo2 time: {toc - tic:0.4f}s")

"""
Implement a a program that  prints a list of 100 numbers. It should tells you if a number is divisible by 3 
prints FIZZ if it's divisible by 5 prints BUZZ and 
if it's divisible by 3 & 5 prints FIZZBUZZ

pseudo code:

- loop 1... 100
- if number is divisible by 3 we print FIZZ
- if the number is divisible by 5 we print BUZZ
- if the number is divisible by 3 & 5 we print FIZZBUZZ

"""
if __name__ == '__main__':
    for n in range(101):
        if n % 3 == 0 and n % 5 == 0:
            print("FIZZBUZZ")
        elif n % 5 == 0:
            print("BUZZ")
        elif n % 3 == 0:
            print("FIZZ")
        else:
            print(n)


def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string
