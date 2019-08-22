class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens = sorted(tokens)
        l = 0
        r = len(tokens)
        ret = 0
        score = 0
        while l<r:
            if P >= tokens[l]:
                P -= tokens[l]
                score+=1
                ret = max(score,ret)
                l+=1
            elif score>0:
                P += tokens[r-1]
                r-=1
                score -= 1
            else:
                break
        return ret
        