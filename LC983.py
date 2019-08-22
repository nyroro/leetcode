class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pi = 0
        for t in popped:
            while pi<len(pushed) and (len(stack)==0 or stack[-1]!=t):
                stack.append(pushed[pi])
                pi+=1
            if len(stack) >0 and stack[-1] == t:
                stack.pop()
            else:
                break
        return len(stack)==0
                