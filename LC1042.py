class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        if len(stones)<=1:
            return 0
        if len(stones) <K:
            return -1
        if len(stones)==K:
            return sum(stones)
        if (len(stones) -1)%(K-1) != 0:
            return -1
        dp = {}
        for i in xrange(len(stones)):
            dp[(i,i)] = stones[i]
        for length in xrange(2, len(stones)+1):
            for i in xrange(0, len(stones) - length+1):
                piles = (length-1)%(K-1)+1
                
                for j in xrange(1,length):
                    l = (i, i+j-1)
                    ll = (j-1)%(K-1)+1
                    r = (i+j, i+length-1)
                    rr = (length - j -1)%(K-1)+1
                    # print l,r
                    if ll+rr>K:
                        continue
                    
                    if (i,i+length-1) not in dp:
                        dp[(i,i+length-1)] = dp[l]+dp[r]
                    else:
                        dp[(i,i+length-1)] = min(dp[(i,i+length-1)],dp[l]+dp[r])
                if piles == 1:
                    dp[(i,i+length-1)] += sum(stones[i:i+length])
        return dp[(0,len(stones)-1)]-sum(stones)
                
            