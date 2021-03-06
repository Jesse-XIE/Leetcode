// Description: 
// ---------------

// Given an array of non-negative integers, you are initially positioned at the first index of the array.
// Each element in the array represents your maximum jump length at that position.
// Determine if you are able to reach the last index.
// For example:
// A = [2,3,1,1,4], return true.
// A = [3,2,1,0,4], return false.



class Solution {
public:
    bool canJump(vector<int>& nums) {
       int jump_remain = 1;
       auto end = --nums.end();
       for (auto it = nums.begin(); it != end; ++it){
           jump_remain = max(jump_remain - 1, *it);
           if(jump_remain == 0) {
               return false;
           }
       }
       return true;
    }
};