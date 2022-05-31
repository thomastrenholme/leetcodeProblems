# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import sys


class Solution:

    
    retVal = sys.maxsize
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        
        


        def getDepth(node, depth):

            print("CurrNode: " + str(node))
            if depth > self.retVal:
                return
            
            if not (node.left or node.right):
                
                if depth < self.retVal:

                    print("New min depth: " + str(depth))

                    self.retVal = depth
                    return
                
            if node.left:
                getDepth(node.left, depth+1)
            if node.right:
                getDepth(node.right, depth+1)
        
        getDepth(root, 1)
        return self.retVal
            

g = Solution()

