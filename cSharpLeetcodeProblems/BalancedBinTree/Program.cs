
 public class TreeNode {
     public int val;
     public TreeNode left;
     public TreeNode right;
     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
            this.val = val;
            this.left = left;
            this.right = right;
      }
 }

public class Solution {

    public bool ans = true;
    public bool IsBalanced(TreeNode root) {
        
        int temp = checkBalance(root);
        return ans;

    }
    public int checkBalance(TreeNode node){
            if(!ans){
                return 0;
            }
            if(node==null){
                return 0;
            }

            int leftTreeDepth= checkBalance(node.left);
            int rightTreeDepth = checkBalance(node.right);

            if(Math.Abs(leftTreeDepth - rightTreeDepth) > 1){
                ans = false;
            }
            return 1 + Math.Max(leftTreeDepth, rightTreeDepth);   
    }
        
}