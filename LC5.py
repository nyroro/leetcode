class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        
        right = 0
        mid = 0
        res = [0] * len(s)
        
        for i in range(len(s)):
            if i < right:
                left = 2 * mid - i
                res[i] = min(res[left], right - i)
            
            while i + res[i] < len(s) and i - res[i] >= 0 and s[i+res[i]] == s[i-res[i]]:
                res[i] += 1
                if i + res[i] > right:
                    right = i + res[i]
                    mid = i
        s_len, i = max([(t, i) for i, t in enumerate(res)])
        ret = s[i - s_len + 1: i + s_len - 1].replace('#', '')
        return ret
        