class Solution:
    def countBits(self, num: int) -> List[int]:
        def bit(n):
            ret = 0
            while n > 0:
                ret += 1
                n -= n&-n
            return ret
        return [bit(t) for t in range(0,num+1)]