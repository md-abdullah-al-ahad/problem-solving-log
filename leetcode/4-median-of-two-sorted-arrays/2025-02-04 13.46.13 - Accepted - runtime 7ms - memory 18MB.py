from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        merged = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < m:
            merged.append(nums1[i])
            i += 1
        while j<n:
            merged.append(nums2[j])
            j += 1
        
        o = len(merged)
        if o % 2 == 0:
            return (merged[o // 2] + merged[o // 2 - 1]) / 2
        else:
            return merged[o // 2]