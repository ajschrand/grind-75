# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Lists with fewer than 2 elements need no reversing
        if not head or not head.next:
            return head
        
        # Pointers that traverse the array while reversing each next value in order
        cur = None
        next = head
        
        while next:
            # Get a pointer to the next iteration's node to flip
            temp = next.next
            
            # Flip the current node's next value
            next.next = cur
            
            # Advance the pointers
            cur = next
            next = temp
            
        return cur