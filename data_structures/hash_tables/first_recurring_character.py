"""
Given an array return the first recurring character
Example:
    ar = [2,5,1,2,3,5,1,2,4]:
    returns 2

    ar = [2,1,1,2,3,5,1,2,4]
    returns 1

    ar = [2,3,4,5]:
    return None
"""


def first_recurring_character(nums): # o(n)
    bucket = {}
    for i, n in enumerate(nums):
        if n not in bucket:
            bucket[n] = i
        elif n in bucket:
            return n
        else:
            return None


nw = [2, 5, 1, 2, 3, 5, 1, 2, 4]
x = first_recurring_character(nw)
print(x)
