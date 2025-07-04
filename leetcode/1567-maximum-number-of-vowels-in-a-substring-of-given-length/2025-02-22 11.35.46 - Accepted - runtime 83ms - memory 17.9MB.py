class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        current = 0
        vowels = "aeiou"
        for i in range (len(s)):
            if s[i] in vowels:
                current+=1
            if i>=k-1:
                ans = max(current,ans)
                if s[i-k+1] in vowels:
                    current-=1
        return ans