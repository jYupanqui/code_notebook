"""
Stacks:
(plates)
LIFO (Last in First Out)

Lookup O(n)
pop O(1)
push O(1)
peek O(1)

Notes:
    - Arrays and linked lists worked to create a stack


Queues:
(waiting line)
FIFO (First in First Out)

lookup O(n)
enqueue O(1)
dequeue O(1)
peek O(1)
Note:
    - Creating a queue from arrays is un-efficient. Removing first in line causes a shifting process O(n).
    - Ideally implement them with linked lists


General Notes:
- Fast operations
- Fast peek
- Ordered
- Slow lookup

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Using Linked Lists
    """

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer
        self.length += 1

        return self

    def pop(self):
        if not self.top:
            return None
        if self.length == 0:
            self.bottom = None

        holding_pointer = self.top
        self.top = self.top.next
        self.length -= 1
        return holding_pointer


myStack = Stack()
myStack.push("google")


class Stack:
    """
    Using Arrays
    """

    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array) - 1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        ret = self.array.pop()
        return ret


# **************** QUEUES ***************

class Queue:
    """
    Using Linked Lists and Node Class from top
    """

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            self.last = None
        holding_pointer = self.first
        self.first = self.first.next
        self.length -= 1

        return holding_pointer
