class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums1) % 2 == 1:
            for num in nums2:
                ans = ans ^ num
        if len(nums2) % 2 == 1:
            for num in nums1:
                ans = ans ^ num
        return ans
