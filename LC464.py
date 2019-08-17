class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if sum(range(maxChoosableInteger+1))<desiredTotal:
            return False
        
        if sum(range(maxChoosableInteger+1))==desiredTotal:
            return maxChoosableInteger%2==1
        if desiredTotal<maxChoosableInteger:
            return True
        dp = [False] * (1<<maxChoosableInteger)
        d = desiredTotal
        m = maxChoosableInteger
        vis = set()
        
        def dfs(total, status):
            if status in vis:
                return dp[status]
            if total >= d:
                return False
            flag = False
            for i in xrange(0, m):
                if status&(1<<i)>0:
                    continue
                flag |= not dfs(total+1+i, status|(1<<i))
                if flag:
                    break
            dp[status] = flag
            vis.add(status)
            return dp[status]
        return dfs(0,0)
            