# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional
class Solution:

    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root
        retDict = defaultdict(list)
        
        retDict[0].append(root.val)
        def dfsTree(node, depth):
            retDict[depth].append(node.val)
            if node.left or node.right:

                if node.left:
                    dfsTree(node.left, depth+1)
                if node.right:
                    dfsTree(node.right, depth+1)
        
        if root.left:
            dfsTree(root.left, 1)
        if root.right:
            dfsTree(root.right, 1)
        return list(retDict.values())