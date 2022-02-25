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

Pro:
    - Fast lookups (Good collision resolution needed)
    - Fast inserts
    - Flexible keys
Cons:
    - Unordered (python dicts are ordered from 3.7)
    - Slow key iteration

"""


class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _my_hash(self, key):
        """
        ORD
        Given a string representing one Unicode character, return an integer representing the Unicode code point of
        that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. T
        his is the inverse of chr().
        :param key:
        :return:
        """

        h = 0
        for i, k in enumerate(key):
            h = (h + ord(k) * i) % len(self.data)
        return h

    def set(self, key, value):
        address = self._my_hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        print(self.data)

    def get(self, key):
        """
        When there is low space it can change to o(n) due too hash collitions
        :param key:
        :return:
        """
        address = self._my_hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for item in current_bucket:
                if item[0] == key:
                    return item[1]
        else:
            return None

    def delete(self, key):
        address = self._my_hash(key)
        if self.data[address]:
            for i, item in enumerate(self.data[address]):
                if item[0] == key:
                    self.data[address].pop(i)

    def keys(self):
        keys_list = []
        for items in self.data:
            if items:
                for key in items:  # This is needed due to collitions
                    keys_list.append(key[0])
        return keys_list

    def values(self):
        val_list = []
        for items in self.data:
            if items:
                for key in items:  # This is needed due to collitions
                    val_list.append(key[1])
        return val_list


table = HashTable(2)
table.set('grapes', 10)
table.set('apples', 20)
table.set('oranges', 23)
table.delete('oranges')
print(table.keys())
print(table.values())
# print(table.get('pepe'))
