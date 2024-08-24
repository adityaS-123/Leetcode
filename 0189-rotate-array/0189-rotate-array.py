class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Normalize k
        
        count = 0  # Number of elements placed correctly
        
        start = 0
        while count < n:
            current_index = start
            current_value = nums[start]
            
            while True:
                next_index = (current_index + k) % n
                nums[next_index], current_value = current_value, nums[next_index]
                current_index = next_index
                count += 1
                
                if start == current_index:
                    break
                
            start += 1
