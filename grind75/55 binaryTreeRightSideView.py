# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return root
        
        treeDepthToValueVisible={}


        ##Go down right on the rightmost path
        ##Go down left on the rightmost path

        

        def traverseDown(currNode, currDepth):

            if currDepth not in treeDepthToValueVisible:
                    treeDepthToValueVisible[currDepth] = currNode.val

            if currNode.right:
                traverseDown(currNode.right, currDepth+1)
            if currNode.left:
                traverseDown(currNode.left, currDepth +1)
        traverseDown(root, 0)

        return treeDepthToValueVisible.values()

