class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if str2[:len(str1)] == str1 and str2[-len(str1):] == str1:
                return True
            return False
        total = 0 
        for i in range (len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    total += 1
        return total
            