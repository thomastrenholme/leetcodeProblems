# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        if max(q.val, p.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(q.val, p.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

g = Solution()

print(g.lowestCommonAncestor(root=TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9))), p=TreeNode(2), q=TreeNode(4)))