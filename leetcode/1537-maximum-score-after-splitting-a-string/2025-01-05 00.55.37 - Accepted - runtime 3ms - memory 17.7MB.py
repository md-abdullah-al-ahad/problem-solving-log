class Solution:
    def maxScore(self, s: str) -> int:
        lst = [0] * len(s)
        for i, c in enumerate(s):
            if c == "1":
                lst[i] = 1
        n = len(lst)
        for i in range(1, n):
            lst[i] += lst[i - 1]
        ans = -1
        zero_count = 0
        for i in range (len(s)-1):
            if s[i] == "0":
                zero_count += 1
            if i == 0:
                ans = max(ans, zero_count + lst[n - 1] - lst[i])
            else:
                ans = max(ans, zero_count + lst[n - 1] - lst[i - 1])

        return ans
