public class Solution {

    public int minDepth = Int32.MaxValue;
    public int MinDepth(TreeNode root) {

        if(root == null){
            return 0;
        }
        getDepth(root, 1);
        return minDepth;
    }

    public void getDepth(TreeNode node, int depth){

        //Stop pointless recursion if already past min depth
        if(depth > minDepth)
        {
            return;
        }
        //Reached leaf node
        if(node.left == null && node.right == null){

            Console.WriteLine("Leaf node, val: " + node.val + " and currMinDepth: " + minDepth);
            if(depth < minDepth){
                minDepth = depth;
                return;
            }
        }

        Console.WriteLine("Curr Node: " + node.val);

        //Both children case
        if(node.left != null && node.right != null){

            getDepth(node.left, depth+1);
            getDepth(node.right, depth+1);
        }

        else if(node.left != null){
            getDepth(node.left, depth+1);
        }
        else if(node.right != null){
            getDepth(node.right, depth+1);
        }
    }
}