class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        frequency = 1
        total = 1
        static_i = 0
        moving_i = 1
        while(moving_i<len(nums)):
            if nums[moving_i]== nums[static_i]:
                frequency+=1
            else:
                frequency=1
            if frequency<=2:
                static_i+=1
                nums[static_i]=nums[moving_i]
                total+=1
            moving_i+=1
        return total