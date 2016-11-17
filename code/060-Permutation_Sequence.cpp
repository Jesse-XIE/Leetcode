// Description: 
// ---------------

// The set [1,2,3,…,n] contains a total of n! unique permutations.
// By listing and labeling all of the permutations in order,
// We get the following sequence (ie, for n = 3):
// "123"
// "132"
// "213"
// "231"
// "312"
// "321"
// Given n and k, return the kth permutation sequence.
// Note: Given n will be between 1 and 9 inclusive.



class Solution {
public:
    string getPermutation(int n, int k) {
        int factoral = 1;
        vector<int> remains;   // the remaining number
        for(int i = 1; i <= n - 1; ++i){
            factoral *= i;
            remains.push_back(i);
        }
        remains.push_back(n);
        string result;
        --k;
        for(int i = n - 1; i >= 1; --i){
            result.append(to_string(remains[k / factoral]));
            remains.erase(remains.begin() + k / factoral);
            k %= factoral;
            factoral /= i;
        }
        result.append(to_string(remains[0]));
        return result;
    }
};