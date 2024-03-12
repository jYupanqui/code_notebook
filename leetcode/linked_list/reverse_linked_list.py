"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """

    :param self:
    :param head:
    :return:
    - Build the list
    - traverse over the list and switch directions
    1 -> 2 -> 3 -> 4 -> 5
    We can use two pointers technique prev and current



    """
    # Iterative TC O(n) SC O(1)
    prev, curr = None, head
    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next
    return prev


    # Recursive TC O(n) SC O(1)

    # if not head:
    #     return None
    # new_head = head
    # if head.next:
    #     new_head = reverse_list(head.next)
    #     head.next.next = head
    # head.next = None

    # return new_head




# this needs to be converted into a linked list and then pass the head to the function.
head = [1,2,3,4,5]
reverse_list(head)
