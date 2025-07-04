class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        length = 1
        for i in range(len(s)-1):
            if ord(s[i])+1 == ord(s[i + 1]):
                length+=1
            else:
                ans = max(length,ans)
                length = 1
        ans = max(length,ans)
        return ans