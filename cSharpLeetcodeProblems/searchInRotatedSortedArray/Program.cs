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
        
        int smallestIdx = l;
        

        if(target >= nums[smallestIdx] && target <= nums[nums.Length -1]){
            l = smallestIdx;
            r = nums.Length -1;
        }
        else{
            l = 0;
            r = smallestIdx;
        }

        while(l <= r){
            int m = l + (r - l)/2;

            if(target > nums[m]){
                l = m +1;
            }
            else if(target < nums[m]){
                r = m -1;
            }
            else{
                return m;
            }
        }
        return -1;


    }
}