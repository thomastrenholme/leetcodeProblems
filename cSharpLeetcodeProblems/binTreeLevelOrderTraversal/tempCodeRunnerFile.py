# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        retDict = {}
        if not root:
            return self.retArr

        
        

        def helperFunc(node, index):
            print("CurrNode: " + str(node.val) + " index: " + str(index))
            if node.left and node.right:
                retDict[index] = [node.left.val, node.right.val]

                helperFunc(node.left, 2*index)
                helperFunc(node.right, 2*index+1)
            elif node.left:
                retDict[index] = [node.left.val]
                helperFunc(node.left, 2*index)
            elif node.right:
                retDict[index] = [node.right.val]
                helperFunc(node.right, 2*index+1)
            


        retDict[0] = [root.val]
        helperFunc(root, 1)

        return list(retDict.values())

g = Solution()

print(g.levelOrder(root=TreeNode(1)))


