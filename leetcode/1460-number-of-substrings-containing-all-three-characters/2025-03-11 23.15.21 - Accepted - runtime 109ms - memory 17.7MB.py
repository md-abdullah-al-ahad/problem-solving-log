class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        i = 0
        for j in range(len(s)):
            char_count[s[j]] += 1
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                ans += len(s) - j
                char_count[s[i]] -= 1
                i += 1
        return ans
