// Description: 
// ---------------

// Given a collection of numbers that might contain duplicates, return all possible unique permutations.
// For example,
// [1,1,2] have the following unique permutations:
// [
//   [1,1,2],
//   [1,2,1],
//   [2,1,1]
// ]



struct ele_count {
    int ele;
    int count;
};
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.begin() + n);
        vector<ele_count> remains;
                ele_count new_ele;
        new_ele.ele = nums[0];
        new_ele.count = 1;
        remains.push_back(new_ele);
        int j = 0;
        for (int i = 1; i != n; ++i){
            if(nums[i] == remains[j].ele){
                remains[j].count += 1;
            } else {
                new_ele.ele = nums[i];
                remains.push_back(new_ele);
                j += 1;
            }
        }
        vector<vector<int>> result;
        vector<int> current;
        permuteRecursive(remains, result, current);
        return result;
    }
        void permuteRecursive(vector<ele_count> &remains, vector<vector<int>> &result, vector<int> &current){
        int n = remains.size();
        bool has_ele = false;
        for(int i = 0; i != n; ++i){
            if (remains[i].count > 0){
                has_ele = true;
                remains[i].count -= 1;
                vector<int> new_current(current);
                new_current.push_back(remains[i].ele);
                permuteRecursive(remains, result, new_current);
                remains[i].count += 1;
            }
                    }
        if (not has_ele){
            result.push_back(current);
        }
    }
};