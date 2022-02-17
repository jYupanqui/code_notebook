"""
Big O:
    Lookup - O(1)
    Push - O(1)
    Insert - O(n)
    Delete - O(n)

Types:
    Static - size it's defined
    Dynamic -  Copies original array into a new one with more memory, expands  as you add more elements. Append can be
                O(n), usually doubles the space.

Pros:
    - Fast lookups
    - Fast push/pop
    - Ordered
Cons:
    - Slow inserts
    - slow deletes
    - Fixed size (static arrays)

You can build any data structure that we want. Example of custom array.
"""


class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return f"MyArray - length:{self.length}, data: {self.data}"

    def get(self, index):
        return self.data.get(index)

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data.get(self.length - 1)
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data.get(index)
        self.shift_items_delete(index)  # Applying single responsibility principle
        return item

    def insert(self, index, item):

        if (index < 0) or (index > self.length - 1):
            msg = f"Index must be between: 0 - {self.length - 1}"
            raise Exception(msg)

        # append at end of array is a push
        if index == self.length - 1:
            self.push(item)
        elif index == 0:  # append at beginning  or array
            for i in range(self.length - 1, -1, -1):
                self.data[i + 1] = self.data[i]

            self.data[index] = item
            self.length += 1
        else:
            for i in range(self.length - 1, 0, -1):
                self.data[i + 1] = self.data[i]

            self.data[index] = item
            self.length += 1

    def shift_items_delete(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


array = MyArray()

array.push("hi")
array.push("you")
array.push("are")
array.push("awesome")
array.push("!")
array.insert(-1, "Josue")

print(array)
