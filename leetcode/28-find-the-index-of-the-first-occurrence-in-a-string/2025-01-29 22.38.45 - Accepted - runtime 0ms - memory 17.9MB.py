class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        for i in range (0,n-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1