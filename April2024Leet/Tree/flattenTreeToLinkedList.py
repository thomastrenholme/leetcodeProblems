from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.node = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

    def preOrderTraverse(self, root):

        if root is not None:
            leftDummy = root.left
            root.left = None

            rightDummy = root.right
            root.right = None

        if leftDummy is not None:
            



