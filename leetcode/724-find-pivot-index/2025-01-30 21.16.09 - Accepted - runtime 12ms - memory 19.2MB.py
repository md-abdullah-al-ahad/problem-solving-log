class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        prefix_sum = nums.copy()
        postfix_sum = nums.copy()
        for i in range (1,len(nums)):
            prefix_sum[i]+=prefix_sum[i-1]
        for i in range (len(nums)-2,-1,-1):
            postfix_sum[i]+=postfix_sum[i+1]
        for i in range (len(nums)):
            if i == 0:
                if postfix_sum[i+1] == 0:
                    return i
            elif i == len(nums)-1:
                if prefix_sum[i-1]==0:
                    return i
            else:
                if prefix_sum[i-1]==postfix_sum[i+1]:
                    return i
        return -1
