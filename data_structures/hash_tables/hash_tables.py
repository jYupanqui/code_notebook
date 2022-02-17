"""
Big O:
    Lookup - O(1)
    Search - O(1)
    Insert - O(1)
    Delete - O(1)

Hash Collisions:
    - https://www.cs.usfca.edu/~galles/visualization/OpenHash.html
    - When collisions appear the lookup performance goes to O(n)
    - Hash tables can assign the same memory space to different entries.

"""


class HashTable:
    def __init__(self, size):
        self.data = []

    def _hash(self, key):
        pass
