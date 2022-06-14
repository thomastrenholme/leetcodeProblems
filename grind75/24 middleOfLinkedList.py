# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        llMap={}

        curr = head
        ctr=0

        while curr:
            
            llMap[ctr]=curr
            ctr+=1
            curr=curr.next
        
        return list(llMap.values())[ctr//2]