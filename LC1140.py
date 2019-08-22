from collections import Counter
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        cnt = Counter(barcodes)
        sorted_cnt = sorted([(-value, key) for key,value in cnt.items()])
        ret = [None] * len(barcodes)
        now = 0
        nowValue = -sorted_cnt[0][0]
        for i in xrange(0,len(ret),2):
            ret[i] = sorted_cnt[now][1]
            nowValue -=1
            if nowValue == 0:
                now+=1
                if now<len(sorted_cnt):
                    nowValue = -sorted_cnt[now][0]
        # print now,nowValue, sorted_cnt[now][1]
        for i in xrange(1,len(ret),2):
            ret[i] = sorted_cnt[now][1]
            nowValue -=1
            if nowValue == 0:
                now+=1
                if now<len(sorted_cnt):
                    nowValue = -sorted_cnt[now][0]
        return ret