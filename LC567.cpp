#include <map>
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int nowSize = s1.size();
        map<char,int> mp;
        for(int i=0;i<s1.size();i++)
        {
            mp[s1[i]]++;
        }
        
        for(int i=0;i<s2.size();i++)
        {
            if(i>=s1.size())
            {
                char c = s2[i-s1.size()];
                if(mp.count(c)!=0)
                {
                    mp[c]++;
                    if(mp[c]>0)
                        nowSize++;
                }
            }
            char c = s2[i];
            if(mp.count(c)!=0)
            {
                mp[c]--;
                if(mp[c]>=0)
                {
                    nowSize--;
                    if(nowSize==0)
                    {
                        return true;
                    }
                }
            }
            // for(auto it = mp.begin();it!=mp.end();it++)
            // {
            //     cout<<it->first<<' '<<it->second<<endl;
            // }
            // cout<<endl;
        }
        return false;
    }
};