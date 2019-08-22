#include<queue>
#define max(a, b) (a>b?a:b)
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int len = nums.size();
        int ret1 = nums[0]*nums[1]*nums[len-1];
        int ret2 = nums[len-1]*nums[len-2]*nums[len-3];
        return max(ret1, ret2);
    }
};