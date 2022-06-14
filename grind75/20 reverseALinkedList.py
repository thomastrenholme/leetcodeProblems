# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from contextlib import nullcontext
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        prev = None
        curr=head

        while curr:
            ##store next node
            currNext = curr.next

            ##set next to prev
            curr.next = prev

            ##update prev
            prev = curr

            ##advance to next node
            curr = currNext
        return prev
        