##Definition for singly-linked list.
from distutils.util import strtobool
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        totalSum=0

        nCtr=0
        while isinstance(l1.next, ListNode):
            totalSum += l1.val * 10**nCtr

            l1 = l1.next
            nCtr+=1

        nCtr=0
        while isinstance(l2.next, ListNode):
            totalSum+=l2.val* 10**nCtr

            l2 = l2.next
            nCtr+=1

        reversedSumString = str(totalSum)[::-1]

        n = ListNode(val=int(reversedSumString[0]))
        lastNode = n
        for digit in reversedSumString[1:]:
            print(digit)
            node= ListNode(val=int(digit))
            print(str(node))
            lastNode.next = node

            lastNode = node


        return n


        