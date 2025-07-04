class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total = 1
        static_i = 0
        moving_i = 1
        while(moving_i<len(nums)):
            if nums[moving_i]!= nums[static_i]:
                total+=1
                static_i+=1
                nums[static_i]=nums[moving_i]
            moving_i+=1
        return total
