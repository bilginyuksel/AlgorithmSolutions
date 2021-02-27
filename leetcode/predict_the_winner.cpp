#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    int predict_memo_util(const vector<int>& nums, int left, int right, int turn,vector<vector<int>> memo){
        if(left >= right)
            return turn * nums[left]; 

        if(memo[left][right] != -1)
            return memo[left][right];

        int scoreNumLeft = turn * nums[left] + predict_memo_util(nums, left+1, right, -turn, memo); 
        int scoreNumRight = turn * nums[right] + predict_memo_util(nums, left, right-1, -turn, memo);  
        memo[left][right] =  turn * max(turn*scoreNumLeft, turn*scoreNumRight);
        return memo[left][right];
    }
    bool predict_the_winner_memo(vector<int> nums) {
        vector<vector<int>> memo(nums.size(), vector<int>(nums.size(), -1));
        return predict_memo_util(nums, 0, nums.size()-1, 1, memo) >= 0; 
    }


    bool predict_the_winner_bottom_up(const vector<int>& nums) {
        vector<vector<int>> moves(nums.size()+1, vector<int>(nums.size()));
        for(int left=nums.size();left>=0;left--){
            for(int right=left+1;right<nums.size();right++){
                int left_score = nums[left] - moves[left+1][right];
                int right_score = nums[right] - moves[left][right-1];
                moves[left][right] = max(left_score, right_score);
            }
        }

        return moves[0][nums.size()-1] >= 0; 
    }

    bool predict_the_winner_bottom_up_less_memory(const vector<int>& nums) {
        vector<int> moves(nums.size()+1);
        for(int left=nums.size();left>=0;left--){
            for(int right=left;right<nums.size();right++){
                int left_score = nums[left] - moves[right]; 
                int right_score = nums[right] + moves[left-1];
                moves[right] = max(left_score, right_score);
            }
        }

        return moves[nums.size()-1] >= 0;
    }
public:
    bool PredictTheWinner(vector<int>& nums) {
        return predict_the_winner_memo(nums);
    }
};

int main() {
    vector<int> nums1{1,5,2};
    vector<int> nums2{1,5,233,7};

    Solution solve;
    bool result = solve.PredictTheWinner(nums1);
    bool result2 = solve.PredictTheWinner(nums2);
    cout<<"Case #1: "<<result<<"\n";
    cout<<"Case #2: "<<result2<<"\n";
}
