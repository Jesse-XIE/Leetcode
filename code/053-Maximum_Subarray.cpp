// Description: 
// ---------------

// Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
// For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
// the contiguous subarray [4,-1,2,1] has the largest sum = 6.
// click to show more practice.



class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = nums[0], sum = nums[0];
        for (auto it = ++nums.begin(); it != nums.end(); ++it){
            sum = max(*it, *it + sum);
            max_sum = max(sum, max_sum);
        }
        return max_sum;
    }
};