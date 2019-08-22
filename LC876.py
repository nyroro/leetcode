from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W != 0:
            return False
        cnter = Counter(hand)
        for key in sorted(cnter.keys()):
            if cnter[key]>0:
                value = cnter[key]
                for i in xrange(key, key+W):
                    cnter[i] -= value
                    if cnter[i]<0:
                        return False
            elif cnter[key] < 0:
                return False
        return sum(cnter.values()) == 0
        