class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase and filter out non-alphanumeric characters
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Check if the filtered string is a palindrome
        return filtered_chars == filtered_chars[::-1]
