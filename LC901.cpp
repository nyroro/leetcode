class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        vector<pair<int, int>> vb(B.size());
        for(int i=0;i<B.size();i++)
        {
            vb[i] = make_pair(-B[i], i);
        }
        sort(vb.begin(), vb.end());
        
        sort(A.begin(), A.end());
        
        vector<int> ret(A.size());
        int l = 0, r = A.size() - 1;
        for(int i=0;i<B.size();i++)
        {
            if(A[r]>-vb[i].first)
            {
                ret[vb[i].second] = A[r];
                r--;
            }
            else
            {
                ret[vb[i].second] = A[l];
                l++;
            }
        }
        return ret;
    }
};