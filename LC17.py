class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        table = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ret = [""]
        for t in digits:
            tmp = []
            chars = table[ord(t) - ord('0')]
            for now in ret:
                for char in chars:
                    tmp.append(now+char)
            ret = tmp
        return ret