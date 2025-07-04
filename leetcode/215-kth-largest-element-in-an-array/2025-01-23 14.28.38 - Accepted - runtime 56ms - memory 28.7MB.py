class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums1 = sorted(nums,reverse = True)
        return nums1[k-1]