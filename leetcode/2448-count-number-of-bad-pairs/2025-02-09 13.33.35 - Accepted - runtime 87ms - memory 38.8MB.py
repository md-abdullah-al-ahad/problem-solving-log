class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {}
        total = 0
        for i in range (len(nums)):
            if nums[i]-i not in hashmap:
                hashmap[nums[i]-i]=1
            else:
                hashmap[nums[i]-i]+=1
        for key in hashmap:
            count = hashmap[key]
            total += (count * (count - 1)) // 2
        return (n * (n - 1)) // 2 - total