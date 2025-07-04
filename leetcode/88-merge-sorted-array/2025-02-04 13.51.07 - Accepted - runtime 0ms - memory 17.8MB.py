class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged_list = []
        i,j = 0,0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                merged_list.append(nums1[i])
                i+=1
            else:
                merged_list.append(nums2[j])
                j+=1
        while i<m:
            merged_list.append(nums1[i])
            i+=1
        while j<n:
            merged_list.append(nums2[j])
            j+=1
        for i in range (m+n):
            nums1[i]=merged_list[i]
        
        