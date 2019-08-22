from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        seq = [0,2,4,6,8,1,3,5,7,9]
        counter = Counter(s)
        res = Counter()
        
        for num in seq:
            num_str = nums[num]
            num_counter = Counter(num_str)
            cnt = 0
            while counter & num_counter == num_counter:
                cnt += 1
                counter -= num_counter
            res[num] = cnt
        ret = ''
        for k,v in res.iteritems():
            ret = ret + str(k)*v
        return ret