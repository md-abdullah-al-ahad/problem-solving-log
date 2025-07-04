class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        total = 0
        char_window = []
        for i in range (len(s)):
            char_window.append(s[i])
            if len(char_window) > 3:
                char_window.pop(0)
            if len(char_window) == 3 and len(set(char_window)) == 3:
                total += 1
        return total
            
