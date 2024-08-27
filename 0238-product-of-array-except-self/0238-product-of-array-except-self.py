class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        # Calculate the prefix product for each element
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate the suffix product for each element
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
