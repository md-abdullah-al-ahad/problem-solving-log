class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        currentPointer = 0
        count = [0]*3
        for num in nums:
            count[num]+=1
        for i in range (len(nums)):
            while count[currentPointer]==0:
                currentPointer+=1
            nums[i]=currentPointer
            count[currentPointer]-=1
        
        