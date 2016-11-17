// Description: 
// ---------------

// Given an array of strings, group anagrams together.
// For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
// Return:
// [
//   ["ate", "eat","tea"],
//   ["nat","tan"],
//   ["bat"]
// ]
// Note: All inputs will be in lower-case.



class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, int> hash;  // map anagrams to indice in result vector
        for (auto &it : strs){
            string s_sort(it);
            sort(s_sort.begin(), s_sort.end());
            auto got = hash.find(s_sort);
            if (got == hash.end()){
                vector<string> new_ana{it};
                result.push_back(new_ana);
                hash[s_sort] = result.size() - 1;
            } else{
                result[got-> second].push_back(it);
            }
        }
        return result;
    }
};