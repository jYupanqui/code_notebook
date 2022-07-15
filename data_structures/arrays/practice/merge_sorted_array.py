"""
Merge two sorted lists
"""


def merge_sorted_arrays1(l1, l2):
    return sorted(l1 + l2)


print(merge_sorted_arrays1([0, 3, 4, 31], [4, 6, 30]))
