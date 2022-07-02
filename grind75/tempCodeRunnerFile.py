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
        treeDepthToZIndexShown={}

        ##Go down left on the rightmost path

        ##Go down right on the rightmost path

        ##Show the depth at that height in the array by the highest Z-index of the path traveled (rightmost: sysmax)
        ##Leftmost: - sysmax

        def traverseDown(currNode, currDepth, zIndex):
            print("Curr Node: " + str(currNode.val) + " currDepth: " + str(currDepth) + " z: " + str(zIndex))

            ##If already recorded, check if current Z Index is more visible
            ##If it is, update curr Z index at depth to higher value and update value visible to currNode
            if currDepth in treeDepthToZIndexShown:
                if zIndex > treeDepthToZIndexShown[currDepth]:
                    treeDepthToZIndexShown[currDepth] = zIndex
                    treeDepthToValueVisible[currDepth] = currNode.val
            else:
                treeDepthToZIndexShown[currDepth] = zIndex
                treeDepthToValueVisible[currDepth] = currNode.val
            
            if currNode.left:
                traverseDown(currNode.left, currDepth +1, zIndex-1)
            if currNode.right:
                traverseDown(currNode.right, currDepth+1, zIndex)

        treeDepthToValueVisible[0]=root.val
        if root.right: traverseDown(root.right, 1, 10**4)
        if root.left: traverseDown(root.left, 1, -10**4)

        return treeDepthToValueVisible.values()

