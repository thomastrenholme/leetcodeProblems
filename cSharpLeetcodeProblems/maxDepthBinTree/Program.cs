public class Solution {

    public int depth = 0;
    public int MaxDepth(TreeNode root) {
        
        if(root== null){
            return 0;
        }
        checkDepth(root, 0);
        return depth;

    }
    public void checkDepth(TreeNode node, int currDepth){

            if(currDepth > depth){
                depth = currDepth;
            }
            if(node==null){
                return;
            }

            if(node.left != null){
                checkDepth(node.left, currDepth+1);
            }
            
            if(node.right != null){
                checkDepth(node.right, currDepth+1);
            }
            
    }
        
}