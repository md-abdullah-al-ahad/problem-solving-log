class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        char_list = [0]*26
        max_freq_list = [0]*26
        for word in words2:
            for c in word:
                char_list[ord(c) - ord('a')]+=1
            for i in range (26):
                max_freq_list[i]=max(max_freq_list[i],char_list[i])
            char_list = [0]*26
        for word in words1:
            for c in word:
                char_list[ord(c)-ord('a')]+=1
            flag = True
            for i in range (26):
                if max_freq_list[i]>char_list[i]:
                    flag = False
                    break
            if flag:
                ans.append(word)
            char_list = [0]*26
        return ans