# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Avoid processing empty lists
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        # Pointers to crawl each list
        list1Pointer = list1
        list2Pointer = list2
        
        # Dummy node to remember the position of the beginning of the list
        head = ListNode()
        # Pointer that swaps between list1Pointer and list2Pointer depending on which one is lower
        # and changes the next reference of the previous node to match
        cur = head
        
        # Traverse the lists, updating cur.next to point to the next node in sorted order
        # until at least one list has been exhausted
        while list1Pointer is not None and list2Pointer is not None:
            if list1Pointer.val <= list2Pointer.val:
                cur.next = list1Pointer
                list1Pointer = list1Pointer.next
            else:
                cur.next = list2Pointer
                list2Pointer = list2Pointer.next
                
            cur = cur.next
        
        # Once one list has been exhausted, the rest of the nodes should come from the other list
        cur.next = list1Pointer if list1Pointer is not None else list2Pointer
        return head.next