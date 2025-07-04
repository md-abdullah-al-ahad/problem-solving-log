class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        total = 0
        set_of_s = set(s)
        for c in set_of_s:
            left = s.find(c)
            right = s.rfind(c)
            total += len(set(s[left+1:right])) 
        return total