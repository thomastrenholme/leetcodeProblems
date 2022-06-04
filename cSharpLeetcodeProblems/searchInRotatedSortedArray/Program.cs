public class Solution {
    public int Search(int[] nums, int target) {
        
        if(nums == null || nums.Length == 0) return -1;

        int l = 0;
        int r = nums.Length -1;

        while(l < r){
            int midpoint = l + (r - l)/2;

            if(nums[midpoint] > nums[r]){
                l = midpoint+1;
            }
            else{
                r = midpoint;
            }
        }
        Console.WriteLine("PivotIdx: " + l);


    }
}