class Solution {
public:
    const int N=10000;
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        
        int len = nums.size();
        if(len==0)return 0;
        vector<long> sums(len+1,0);
        sums[0] = nums[0];
        for(int i=1;i<nums.size();i++)
        {
            sums[i]=sums[i-1]+nums[i];
        }
        return merge(sums, lower, upper, 0, len);
    }
    
    int merge(vector<long>& sums, int lower, int upper, int low, int high)
    {
        if(high<=low)return 0;
        if(low+1 == high)
        {
            if(sums[low]<=upper && sums[low]>=lower)
                return 1;
            else
                return 0;
        }
        int mid = (low+high)/2;
        int x = mid;
        int y = mid;
        int ret = merge(sums,lower,upper,low,mid)+merge(sums,lower,upper,mid,high);
        for(int i=low;i<mid;i++)
        {
            while(x<high&&sums[x]-sums[i]<lower)x++;
            while(y<high&&sums[y]-sums[i]<=upper)y++;
            ret+=y-x;
        }
        inplace_merge(sums.begin()+low, sums.begin()+mid, sums.begin()+high);
        return ret;
        
    }
    
    
};