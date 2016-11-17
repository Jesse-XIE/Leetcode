// Description: 
// ---------------

// Given an array of non-negative integers, you are initially positioned at the first index of the array.
// Each element in the array represents your maximum jump length at that position.
// Your goal is to reach the last index in the minimum number of jumps.
// For example:
// Given array A = [2,3,1,1,4]
// The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
// Note:
// You can assume that you can always reach the last index.



#include <iostream>
using namespace std;
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int this_step_bound = 0;
        int next_step_bound = 1;
        int step = 0;
        for (int i = 0; i <= n - 2; ++i){
            next_step_bound = max(next_step_bound, nums[i] + i);
            if (i == this_step_bound){
                this_step_bound = next_step_bound;
                step += 1;
            }
        }
        return step;
    }
};