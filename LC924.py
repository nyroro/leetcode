class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        table = {}
        sumA = sum(A)
        for i, t in enumerate(A):
            table[sumA - 2*t] = t
        
        sumB = sum(B)
        for i, t in enumerate(B):
            num = sumB - 2*t
            if num in table:
                return [table[num], t]
        