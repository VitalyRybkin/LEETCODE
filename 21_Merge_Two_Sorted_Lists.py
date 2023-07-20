"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None and list2 is None:
        head = None
    elif list1 is None:
        head = list2
    elif list2 is None:
        head = list1
    else:
        if list1.val <= list2.val:
            head = tail = list1
            list1 = list1.next
            if list1 is None:
                tail.next = list2
        else:
            head = tail = list2
            list2 = list2.next
            if list2 is None:
                tail.next = list1
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            elif list1.val > list2.val:
                tail.next = list2
                tail = list2
                list2 = list2.next
            else:
                tail.next = list1
                tail = list1
                list1 = list1.next
                tail.next = list2
                tail = list2
                list2 = list2.next


        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
    return head


# head = mergeTwoLists(ListNode(1, next=ListNode(2, next=ListNode(val=3, next=None))),
#                      ListNode(0, next=ListNode(3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
# head = mergeTwoLists(ListNode(1, next=None), ListNode(0, next=None))
head = mergeTwoLists(ListNode(1, next=None), ListNode(0, next=None))

tail = head
while tail is not None:
    print(tail.val)
    tail = tail.next

