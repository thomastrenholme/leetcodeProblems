class testClass{
    static void Main(String[] args){

        Solution g = new Solution();
        int ret = g.RemoveElement(new int[] {3, 2, 2, 3}, 3);
        Console.WriteLine("Return value: " + ret);
    }
}



public class Solution {
    public int RemoveElement(int[] nums, int val) {
        
        List<int> idxs = new List<int>();

        for(int i = 0; i < nums.Length; i++){
            
            if(nums[i] == val){
                idxs.Add(i);
            }
        }

        int newCtr = 0;

        int relocatorIdx = 0;
        for(int i = 0; i < nums.Length; i++){
            //Start the relocation at current idx
            relocatorIdx = i;
            //Need to move it away from first (nums.Length - idxs.Count) elements
            if(idxs.Contains(i) && i < (nums.Length - idxs.Count)){
                relocatorIdx+=1;

                //While the relocation idx is one of the idxs we don't want, increment it.
                while(idxs.Contains(relocatorIdx)){
                    relocatorIdx+=1;
                }
                //Console.WriteLine("Swapping idx: " + i + " with: " + relocatorIdx);

                //Perform swap
                int temp = nums[i];
                nums[i] = nums[relocatorIdx];
                nums[relocatorIdx] = temp;

                //Remove the index from the list of bad num indexes
                //Add the new index of the (bad num) to the list of bad num indexes
                idxs.Remove(i);
                idxs.Add(relocatorIdx);
            }
        }
        return (nums.Length - idxs.Count);
    }
}



