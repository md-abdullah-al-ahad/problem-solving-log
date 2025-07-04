class Solution:
    def findValidPair(self, s: str) -> str:
        lst = [0] * 10
        for val in s:
            lst[int(val)] += 1
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if lst[int(s[i])] == int(s[i]) and lst[int(s[i + 1])] == int(s[i + 1]):
                    ans = s[i] + s[i + 1]
                    return ans
        return ""

