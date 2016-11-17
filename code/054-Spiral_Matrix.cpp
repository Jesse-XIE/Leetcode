// Description: 
// ---------------

// Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
// For example,
// Given the following matrix:
// [
//  [ 1, 2, 3 ],
//  [ 4, 5, 6 ],
//  [ 7, 8, 9 ]
// ]
// You should return [1,2,3,6,9,8,7,4,5].



class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        if (not matrix.size()){
            return result;
        }
        spiralOrder_recuresive(matrix, 0, matrix[0].size(), 0, matrix.size(), result);
        return result;
    }
        void spiralOrder_recuresive(vector<vector<int>>& matrix, int i1, int i2, int j1, int j2, vector<int> &result){
        if (i1 == i2 or j1 == j2) return;
        if (i2 == i1 + 1){
            for(int j = j1; j != j2; ++j){
                result.push_back(matrix[j][i1]);
            }
        }
        else if (j2 == j1 + 1){
            for(int i = i1; i != i2; ++i){
                result.push_back(matrix[j1][i]);
            }
        }
        else{
            for(int i = i1; i != i2; ++i){
                result.push_back(matrix[j1][i]);
            }
            for(int j = j1 + 1; j != j2; ++j){
                result.push_back(matrix[j][i2 - 1]);
            }
            for(int i = i2 - 2; i >= i1; --i){
                result.push_back(matrix[j2 - 1][i]);
            }
            for(int j = j2 -2; j != j1; --j){
                result.push_back(matrix[j][i1]);
            }
            spiralOrder_recuresive(matrix, i1 + 1, i2 - 1, j1 + 1, j2 - 1, result);
        }
    }
};