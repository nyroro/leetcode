#include<algorithm>
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(), d.end(), cmp);
        for(auto it=d.begin();it!=d.end();it++)
        {
            if(find(s,*it))
            {
                return *it;
            }
        }
        return "";
    }
    
    static bool cmp(const string &a, const string &b)
    {
        if(a.size()==b.size())
        {
            return a<b;
        }
        return a.size()>b.size();
    }
    bool find(string &s, string &d)
    {
        int i=0, j=0;
        while(i<s.size()&&j<d.size())
        {
            if(s[i]==d[j])
            {
                j++;
            }
            i++;
        }
        return j==d.size();
    }
};