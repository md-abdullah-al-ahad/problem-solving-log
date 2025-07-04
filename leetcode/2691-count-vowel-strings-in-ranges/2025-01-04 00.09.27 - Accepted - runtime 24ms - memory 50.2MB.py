class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'} 
        hash_map = [0] * len(words)
        ans = []
        for i,word in enumerate(words):
            if word[0] in vowels and word[len(word)-1] in vowels:
                hash_map[i]=1
        l = len(hash_map)
        for i in range (1,l):
            hash_map[i]=hash_map[i]+hash_map[i-1]
        for query in queries:
            if query[0]==0:
                ans.append(hash_map[query[1]])
            else:
                ans.append(hash_map[query[1]]-hash_map[query[0]-1])
        return ans
