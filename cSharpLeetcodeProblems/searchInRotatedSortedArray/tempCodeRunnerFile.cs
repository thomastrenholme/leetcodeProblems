public class Solution {

    static void Main(string[] args){
        Console.WriteLine("P");
    }
    public int Search(int[] nums, int target) {
        

        int l = 0;
        int r = nums.Length -1;

        while(l < r){
            int midpoint = l + (l-r)/2;

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