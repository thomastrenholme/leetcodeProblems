# Definition for singly-linked list.
from platform import node
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "[Node. Val: " + str(self.val) + "] Next: " + str(self.next)

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head

        currNode = head
        
        while currNode.next:

            nextNode = currNode.next
            tmpVal = nextNode.val
            nextNode.val = currNode.val
            currNode.val = tmpVal
            if not nextNode.next:
                return head

            currNode = nextNode.next
        return head
            

head = ListNode(2, next = ListNode(5, next = ListNode(3, next = ListNode(4, next = ListNode(6, next= ListNode(2, next=ListNode(2)))))))

head2 = ListNode(1, next = ListNode(2))
g = Solution()

print("\n\n")
print( g.swapPairs(head))