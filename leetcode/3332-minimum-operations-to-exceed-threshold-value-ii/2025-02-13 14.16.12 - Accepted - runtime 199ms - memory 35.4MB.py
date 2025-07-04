class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        while nums[0]<k:
            heappush(nums, 2*heappop(nums) + heappop(nums))
            ans += 1
        return ans