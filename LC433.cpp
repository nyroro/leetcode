class Solution {
public:
    const int N = 300;
    bool connect(string a, string b)
    {
        int cnt=0;
        for(int i=0;i<a.size();i++)
        {
            if(a[i]!=b[i])cnt++;
        }
        return cnt == 1;
    }
    int minMutation(string start, string end, vector<string>& bank) {
        int map[N][N];
        map[0][0] = 0;
        int endIndex=-1;
        
        for(int i=0;i<bank.size();i++)
        {
            if(connect(start, bank[i]))
            {
                map[0][i+1] = map[i+1][0] = 1;
            }
            else
            {
                map[0][i+1] = map[i+1][0] = 0xffff;
            }
            if(bank[i] == end)
            {
                endIndex = i+1;
            }
        }
        if(endIndex<0)
        {
            return -1;
        }
        for(int i=0;i<bank.size();i++)
        {
            map[i+1][i+1] = 0;
            for(int j=i+1;j<bank.size();j++)
            {
                if(connect(bank[i], bank[j]))
                {
                    map[i+1][j+1] = map[j+1][i+1] = 1;
                }
                else
                {
                    map[i+1][j+1] = map[j+1][i+1] = 0xffff;
                }
            }
        }
        for(int i=0;i<=bank.size();i++)
        {
            for(int j=0;j<=bank.size();j++)
            {
                for(int k=0;k<=bank.size();k++)
                {
                    map[i][j] = min(map[i][j], map[i][k]+map[k][j]);
                }
            }
        }
        if(map[0][endIndex]==0xffff)
        {
            return -1;
        }
        return map[0][endIndex];
    }
};