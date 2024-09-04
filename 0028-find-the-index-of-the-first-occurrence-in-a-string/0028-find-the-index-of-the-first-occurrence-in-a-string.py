class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Handle the case when needle is an empty string
        if not needle:
            return 0
        
        # Get the lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # Loop through the haystack to find the first occurrence of needle
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring from the current index matches the needle
            if haystack[i:i + needle_len] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1
