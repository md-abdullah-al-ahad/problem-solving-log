class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_set = {}
        for num in nums:
            if num not in hash_set:
                hash_set[num]=1
            else:
                hash_set[num]+=1
        for key in hash_set:
            if hash_set[key]>(len(nums)//2):
                return key
        