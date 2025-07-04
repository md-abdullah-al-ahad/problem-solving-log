class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zero_count = 0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1]=0
        for i in range (len(nums)):
            if nums[i]==0:
                zero_count+=1
        i = 0
        for j in range (len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        for j in range (i,len(nums)):
            nums[j]=0
        return nums
