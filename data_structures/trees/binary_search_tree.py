"""
Binary Search Tree:

- Better than O(n)
- Ordered
- Flexible size
- No O(1) operations

Balanced
lookup O(log N)
insert O(log N)
delete O(log N)

Unbalanced
lookup O(n)
insert O(n)
delete O(n)

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    # Left
                    if not current_node.left:
                        current_node.left = new_node
                        return self.root

                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        return self.root
                    current_node = current_node.right

    def lookup(self, value):
        if not self.root:
            return False

        current_node = self.root

        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif current_node.value == value:
                return current_node

        return None

    def remove(self, value):
        pass


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)

tree.insert(15)
tree.insert(1)
