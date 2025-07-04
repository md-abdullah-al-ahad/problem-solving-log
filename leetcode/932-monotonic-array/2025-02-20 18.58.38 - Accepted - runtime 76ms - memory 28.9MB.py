class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        check_dec = 0
        check_inc = 0
        for i in range (len(nums)-1):
            if nums[i]<nums[i+1]:
                check_dec += 1
            if nums[i]>nums[i+1]:
                check_inc += 1
        if check_dec == 0 or check_inc == 0:
            return True
        return False
            