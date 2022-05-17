##Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
    
        lowestVal = -sys.maxsize

        amt = self.returnNumGoodNodes(root, lowestVal)
        return amt

    def returnNumGoodNodes(self, root, maxVal):

        print("currNode: " + str(root))
        ##leaf node case
        if root.left==None and root.right == None:
            if root.val >= maxVal:
                return 1
            return 0

        elif root.left==None:
            if root.val > maxVal:
                return (1+self.returnNumGoodNodes(root.right, root.val))
            return self.returnNumGoodNodes(root.right, maxVal)
        
        elif root.right==None:
            if root.val > maxVal:
                return (1+self.returnNumGoodNodes(root.left, root.val))
            return self.returnNumGoodNodes(root.left, maxVal)
        else:
            ##has both
            if root.val > maxVal:
                return (1 + self.returnNumGoodNodes(root.left, root.val) + self.returnNumGoodNodes(root.right, root.val))
            return (self.returnNumGoodNodes(root.left, maxVal) + self.returnNumGoodNodes(root.right, maxVal))

        

        