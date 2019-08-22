from collections import Counter
class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        if len(board) == 0:
            return 0
        data = []
        now = board[0]
        cnt = 1
        for i in xrange(1, len(board)):
            if board[i]==board[i-1]:
                cnt+=1
            else:
                data.append((now,cnt))
                now = board[i]
                cnt = 1
        data.append((now, cnt))
        nums = Counter(hand)
        ret = [0x7fffffff]
        def dfs(data, nums, cnt):
            if len(data)==0:
                ret[0] = min(ret[0], cnt)
                return
            if cnt>ret[0]:
                return
            
            for i in xrange(len(data)):
                x,x_cnt = data[i]
                if 3-x_cnt <= nums[x]:
                    new_data = data[0:i]+data[i+1:len(data)]
                    new_nums = nums - Counter(x*(3-x_cnt))
                    new_cnt = cnt + 3-x_cnt
                    while True:
                        for i in xrange(1, len(new_data)):
                            lx,l_cnt = new_data[i-1]
                            rx,r_cnt = new_data[i]
                            if lx == rx:
                                if l_cnt+r_cnt>=3:
                                    new_data = new_data[0:i-1]+new_data[i+1:]
                                else:
                                    new_data = new_data[0:i-1]+[(lx, l_cnt+r_cnt)]+new_data[i+1:]
                                break
                        else:
                            break
                    dfs(new_data, new_nums, new_cnt)
        dfs(data, nums, 0)
        if ret[0] == 0x7fffffff:
            ret = -1
        else:
            ret = ret[0]
        return ret