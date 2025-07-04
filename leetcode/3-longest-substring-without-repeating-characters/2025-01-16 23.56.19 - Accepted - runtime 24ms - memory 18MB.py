class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha_set=set()
        i,j = 0,0
        length = 0
        while j<len(s):
            while s[j] in alpha_set:
                alpha_set.remove(s[i])
                i+=1
            alpha_set.add(s[j])
            length=max(length,j - i + 1)
            j+=1
        return length