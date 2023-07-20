"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_node = head
        counter = 0
        rem_node = head
        if head is None:
            return head
        while cur_node.next is not None:
            cur_node = cur_node.next
            counter += 1
            if counter > n:
                rem_node = rem_node.next

        if rem_node == cur_node or (n - counter == 1 and rem_node == head):
            head = head.next
            return head

        if n == 1 and rem_node == head and counter == n:
            rem_node.next = None
            return head

        rem_node.next = rem_node.next.next

        return head


