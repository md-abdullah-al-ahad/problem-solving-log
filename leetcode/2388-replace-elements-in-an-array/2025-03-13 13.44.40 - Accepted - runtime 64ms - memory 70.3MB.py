class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for operation in operations:
            nums[hashmap[operation[0]]]=operation[1]
            hashmap[operation[1]]=hashmap[operation[0]]
        return nums
            