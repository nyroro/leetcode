import copy
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        sums = copy.copy(piles)
        for i in xrange(1, len(sums)):
            sums[i] += sums[i-1]
        dp = [[0]*len(piles) for i in xrange(len(piles))]
        for i in xrange(len(piles)):
            dp[i][i] = piles[i]
        for length in xrange(1, len(piles)):
            for i in xrange(len(piles)):
                if i + length < len(piles):
                    range_sum = sums[i+length]
                    if i > 0:
                        range_sum -= sums[i-1]
                    a = range_sum - dp[i+1][i+length]
                    b = range_sum - dp[i][i+length-1]
                    dp[i][i+length] = max(a, b)
                    # print i, i+length, range_sum
        return dp[0][len(piles)-1] > sums[len(piles)-1]/2
        