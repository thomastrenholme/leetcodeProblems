# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        visited=set()
        currNode = head
        while currNode.next:
            if id(currNode) in visited:
                return True
            visited.add(id(currNode))
            currNode=currNode.next
        return False