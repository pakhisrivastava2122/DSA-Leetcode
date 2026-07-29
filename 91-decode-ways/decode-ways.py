class Solution:
    def numDecodings(self, s: str) -> int:
        memo ={}
        def rec(idx):
            if idx==len(s):
                return 1 
            if s[idx]=='0':
                return 0 
            if idx in memo :
                return memo[idx]
            pattern = rec(idx+1)
            if 10<=int(s[idx:idx+2])<=26:
                pattern+=rec(idx+2)
            memo[idx]=pattern 
            return memo[idx]
        return rec(0)