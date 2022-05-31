# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        retDict = {}
        retDict = defaultdict(list)
        if not root:
            return retDict

        
        

        def helperFunc(node, index):
            print("CurrNode: " + str(node.val) + " index: " + str(index))
            if node.left and node.right:
                retDict[index].append(node.left.val), retDict[index].append(node.right.val)

                helperFunc(node.left, 2*index)
                helperFunc(node.right, 2*index)
            elif node.left:
                retDict[index].append(node.left.val)
                helperFunc(node.left, 2*index)
            elif node.right:
                retDict[index].append(node.right.val)
                helperFunc(node.right, 2*index)
            


        retDict[0].append(root.val)
        helperFunc(root, 1)

        return list(retDict.values())

g = Solution()

print(g.levelOrder(root=TreeNode(1)))


