class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = [0] * 26
        second_word = [0] * 26
        for c in s:
            first_word[ord(c) - ord('a')] += 1
        for c in t:
            second_word[ord(c) - ord('a')] += 1
        for i in range(26):
            if first_word[i] != second_word[i]:
                return False
        return True
