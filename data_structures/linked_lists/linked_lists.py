"""


Big O:
    - Prepend o(1)
    - Append o(1)
    - Lookup o(n)
    - Insert o(n)
    - Delete o(n)

Notes:
    - First node is the head
    - Last node is the tail
    - Linked lists are Null terminated
    - Fast insertion
    - Fast Deletion
    - Ordered
    - Flexible Size
    - Slow lookup
    - More memory



Single:
    Pros
        - Less memory
        - Fast insertion and deletion
    Cons:

Double:
    Pros
        - Iterated from any direction
        - Better searching
    Cons:
        - More memory
        - Increased complexity
        -

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = Node
        self.next = None

    def __repr__(self):
        return str({
            "value": self.value,
            "prev": self.prev,
            "next": self.next
        })


class SinglyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return f"List: {self.head} \nLength: {self.length}"

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        # TODO: add params check
        if index >= self.length - 1:
            return self.append(value)
        new_node = Node(value)
        leader = self.traverse_to_index(index - 1)
        temp_pointer = leader.next
        leader.next = new_node
        new_node.next = temp_pointer
        self.length += 1

    def remove(self, index):
        # TODO: add params check
        leader = self.traverse_to_index(index - 1)
        node_to_delete = leader.next
        leader.next = node_to_delete.next
        self.length -= 1

    def traverse_to_index(self, index):
        counter = 0
        node = self.head
        while counter != index:
            node = node.next
            counter += 1
        return node

    def print_list(self):
        list_form = []
        node = self.head
        while node:
            list_form.append(node.value)
            node = node.next

        print(list_form)


# ll = SinglyLinkedList(10)
#
# ll.append(5)
# ll.append(6)
# ll.prepend(1)
# ll.print_list()
# ll.insert(2, 99)
# ll.print_list()
# ll.remove(1)
# ll.print_list()
#
# print(ll)


class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return f"List: {self.head} \nLength: {self.length}"

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        # TODO: add params check
        if index >= self.length - 1:
            return self.append(value)
        new_node = Node(value)
        leader = self.traverse_to_index(index - 1)
        follower = leader.next
        leader.next = new_node
        new_node.prev = leader
        new_node.next = follower
        follower.prev = new_node
        self.length += 1

    def remove(self, index):
        # TODO: add params check
        leader = self.traverse_to_index(index - 1)
        node_to_delete = leader.next
        follower = node_to_delete.next
        leader.next = follower
        follower.prev = leader
        self.length -= 1

    def reverse(self):
        if not self.head.next:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head.next = None
        self.head = first

    def traverse_to_index(self, index):
        counter = 0
        node = self.head
        while counter != index:
            node = node.next
            counter += 1
        return node

    def print_list(self):
        list_form = []
        node = self.head
        while node:
            list_form.append(node.value)
            node = node.next

        print(list_form)


ll = DoublyLinkedList(10)

ll.append(5)
ll.append(6)
ll.prepend(1)
ll.print_list()
ll.insert(2, 99)
ll.print_list()
ll.remove(1)
ll.print_list()
ll.reverse()
ll.print_list()
