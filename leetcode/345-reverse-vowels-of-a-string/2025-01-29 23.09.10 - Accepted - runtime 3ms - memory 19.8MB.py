class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        vowels = "aeiouAEIOU"
        lst = []
        for i in range(len(s)):
            if s[i] in vowels:
                lst.append(i)
        left = 0
        right = len(lst) - 1
        while left < right:
            list_s[lst[left]], list_s[lst[right]] = list_s[lst[right]], list_s[lst[left]]
            left += 1
            right -= 1
        return ''.join(list_s)