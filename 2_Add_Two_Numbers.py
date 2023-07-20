"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = num2 = 0
    multiply = 1
    while l1 is not None or l2 is not None:
        if l1 is not None:
            num1 = num1 + l1.val * multiply
            l1 = l1.next
        if l2 is not None:
            num2 = num2 + l2.val * multiply
            l2 = l2.next
        multiply *= 10

    num = num1 + num2
    head = tail = ListNode(num % 10)
    tail.next = None
    num //= 10
    while num != 0:
        val = num % 10
        num //= 10
        tail.next = ListNode(val)
        tail = tail.next

    return head


head = addTwoNumbers(ListNode(1, next=ListNode(2, next=ListNode(val=3, next=None))),
                     ListNode(0, next=ListNode(3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))

cur = head
while cur is not None:
    print(cur.val)
    cur = cur.next
