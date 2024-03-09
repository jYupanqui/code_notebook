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
    if n in [0,1]:
        return n

    return fibonacci_of(n-1) + fibonacci_of(n-2)

tic = time.perf_counter()
print([fibonacci_of(n) for n in range(40)])
toc = time.perf_counter()
print(f"fibo1 time: {toc-tic:0.4f}s")


# Improvement with memoization
cache = {0:0, 1:1}

def fibonacci_mem_of(n):
    if n in cache:
        return cache[n]

    cache[n] = fibonacci_mem_of(n-1) + fibonacci_mem_of(n-2)
    return cache[n]


tic = time.perf_counter()
print([fibonacci_of(n) for n in range(40)])
toc = time.perf_counter()
print(f"fibo2 time: {toc-tic:0.4f}s")
