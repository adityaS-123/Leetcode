class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        p1 = m - 1  # Last element in nums1's valid part
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # Last element in nums1
        
        # Compare and fill from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
