# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        setOfNodes=set()

        currNode = head

        newListHead=prev=head

        ##Reverse list
        while currNode.next:
            ##store next
            tmp = currNode.next
            ##set next to prev
            currNode.next = prev
            ##change prev to current
            prev = currNode
            ##update currNode to next
            currNode = tmp

        ##list is reversed

            