class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ans = []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            ans.append(list(sorted_frequency.keys())[i])
        
        return ans
