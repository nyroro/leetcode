class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        for t in list(s):
            if t not in table:
                table[t]=1
            else:
                table[t]+=1
        table2 = {}
        ret = 0
        for t in list(s):
            if t not in table2:
                table2[t]=1
            else:
                table2[t]+=1
            table[t]-=1
            if table[t]<=0:
                table.pop(t)
                
            if len(table) == len(table2):
                ret += 1
        return ret