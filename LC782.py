class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        ret = 0
        for t in S:
            if t in J:
                ret+=1
        return ret