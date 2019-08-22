class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def get_num(x):
            ret = 0
            for t in list(x):
                ret = ret*2 + ord(t)-ord('0')
            return ret
        def to_bin(x):
            if x == 0:
                return "0"
            ret = []
            while x > 0:
                ret.append(str(x%2))
                x /= 2
            return ''.join(ret[::-1])
        return to_bin(get_num(a)+get_num(b))
        