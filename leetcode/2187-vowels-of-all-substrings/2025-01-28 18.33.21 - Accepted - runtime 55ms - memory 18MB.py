class Solution:
    def countVowels(self, word: str) -> int:
        vowels = 'aeiou'
        total = 0
        for i,c in enumerate(word):
            if c in vowels:
                total+=(i + 1) * (len(word) - i)
        return total