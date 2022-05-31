/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {

    public Dictionary<int, List<int>> retDict;
    public IList<IList<int>> LevelOrder(TreeNode root) {
        
        retDict = new Dictionary<int, List<int>>();
        if(root == null){
            return (retDict.Values.ToList()).Cast<IList<int>>().ToList();
        }
        retDict[0] = new List<int>();
        retDict[0].Add(root.val);

        helperFunc(root, 1);

        return (retDict.Values.ToList()).Cast<IList<int>>().ToList();

    }

    public void helperFunc(TreeNode node, int index){
        Console.WriteLine("CurrNode: " + node.val + " CurrIdx: " + index);
        if((node.left != null || node.right != null ) && !retDict.ContainsKey(index)){
            retDict[index] = new List<int>();
        }
        if(node.left != null && node.right != null){

            retDict[index].Add(node.left.val); retDict[index].Add(node.right.val);

            helperFunc(node.left, index+1);
            helperFunc(node.right, index+1);
        }
        else if(node.left != null){
            retDict[index].Add(node.left.val);
            helperFunc(node.left, index+1);
        }
        else if(node.right != null){
            retDict[index].Add(node.right.val);
            helperFunc(node.right, index+1);
        }
    }
    
}