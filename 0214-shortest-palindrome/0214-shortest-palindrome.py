class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # If the string is empty or already a palindrome
        if not s or s == s[::-1]:
            return s
        
        # Create the new string with reverse
        new_s = s + "#" + s[::-1]
        
        # Compute the KMP failure array
        n = len(new_s)
        lps = [0] * n
        
        for i in range(1, n):
            j = lps[i - 1]
            
            # Adjust j until we find a match or reach the beginning
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            
            # If there's a match, extend the lps value
            if new_s[i] == new_s[j]:
                j += 1
            
            lps[i] = j
        
        # Use the value in the lps array to determine the longest palindrome prefix
        longest_palindrome_len = lps[-1]
        
        # Add the non-palindrome suffix (reversed) to the front
        non_palindrome_suffix = s[longest_palindrome_len:][::-1]
        
        return non_palindrome_suffix + s
