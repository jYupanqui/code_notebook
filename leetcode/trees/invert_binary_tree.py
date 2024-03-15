"""
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """

    :param root:
    :return:


    """

    if not root:
        return None

    # swap the children
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert_tree(root.left)
    invert_tree(root.right)
    return root


# Input: root = [4,2,7,1,3,6,9]

r = TreeNode(val=4)

r.left = TreeNode(val=2)
r.right = TreeNode(val=7)

r.left.left = TreeNode(val=1)
r.left.right = TreeNode(val=3)

r.right.left = TreeNode(val=6)
r.right.right = TreeNode(val=9)

res = invert_tree(r)
print(res)
