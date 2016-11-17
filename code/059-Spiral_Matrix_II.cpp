// Description: 
// ---------------

// Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
// For example,
// Given n = 3,
// You should return the following matrix:
// [
//  [ 1, 2, 3 ],
//  [ 8, 9, 4 ],
//  [ 7, 6, 5 ]
// ]



class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
       vector<vector<int>> result(n, vector<int>(n, 0));
       fill_recursive(result, 0, n, 1);
       return result;
    }
    void fill_recursive(vector<vector<int>> &result, int step, int n, int curr){
        if (n - step * 2 == 1) {
            result[step][step] = curr;
        }
        if(step < (n + 1) / 2){
            for(int j = step; j != n - step - 1; ++j){
                result[step][j] = curr++;
            }
            for(int i = step; i != n - step - 1; ++i){
                result[i][n - step - 1] = curr++;
            }
            for(int j = n - step - 1; j != step; --j){
                result[n - step - 1][j] = curr++;
            }
            for(int i = n - step - 1; i != step; --i){
                result[i][step] = curr++;
            }
            fill_recursive(result, step + 1, n, curr);
        }
    }
};