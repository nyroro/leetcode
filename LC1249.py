class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, t in enumerate(s):
            if t == '(':
                stack.append(('(', i))
            elif t== ')':
                if len(stack) > 0 and stack[-1][0] == '(':
                    stack = stack[:-1]
                else:
                    stack.append((')', i))
        ret = ''
        now = 0
        for t in stack:
            ret += s[now:t[1]]
            now = t[1]+1
        if now < len(s):
            ret += s[now:]
        return ret
            
        