// Description: 
// ---------------

// Given a collection of distinct numbers, return all possible permutations.
// For example,
// [1,2,3] have the following permutations:
// [
//   [1,2,3],
//   [1,3,2],
//   [2,1,3],
//   [2,3,1],
//   [3,1,2],
//   [3,2,1]
// ]



class Solution {
public:
    vector<vector<int> > permute(vector<int> &nums) {
        vector<vector<int> > result;
        int n = nums.size();
        permute_recursive(nums, n, 0, result);
        return result;
    }
        void permute_recursive(vector<int>& nums, int n, int i, vector<vector<int> > &result){
        if(i == n){
            result.push_back(nums);
            return;
        }
        for(int j = i; j < n; ++j){
            swap(nums[i], nums[j]);
            permute_recursive(nums, n, i + 1, result);
            swap(nums[j], nums[i]);
        }
        return;
    }
};