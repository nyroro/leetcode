class Solution {
public:
    int N = 2000;
    int INF = 0xffff;
    int minCut(string s) {
        bool isPalindrome[N][N];
        int dp[N];
        for(int i=0;i<s.size();i++)
        {
            for(int j=i;j<s.size();j++)
            {
                if(i==j)
                    isPalindrome[i][j]=true;
                else
                {
                    bool flag=true;
                    for(int k=0;k<=j-i;k++)
                    {
                        if(s[i+k]!=s[j-k])
                        {
                            flag=false;
                            break;
                        }
                    }
                    isPalindrome[i][j] = flag;
                }
            }
            dp[i] = INF;
        }
        dp[0] = 1;
        for(int i=1;i<s.size();i++)
        {
            if(isPalindrome[0][i])
            {
                dp[i]=1;
            }
            for(int j=1;j<=i;j++)
            {
                if(isPalindrome[j][i])
                {
                    dp[i] = min(dp[i], dp[j-1]+1);
                }
            }
        }
        return dp[s.size()-1]-1;
    }
};