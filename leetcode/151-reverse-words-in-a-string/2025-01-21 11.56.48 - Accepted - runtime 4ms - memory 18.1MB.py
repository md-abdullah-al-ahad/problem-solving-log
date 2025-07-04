class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        s = s.strip()
        n = len(s)
        current_word = ""
        
        for i in range(n-1, -1, -1):
            if s[i] == " ":
                if current_word:
                    ans+=(current_word[::-1]) + " "
                    current_word = ""
            else:
                current_word += s[i]
        if current_word:
            ans+=(current_word[::-1])
        return ans
