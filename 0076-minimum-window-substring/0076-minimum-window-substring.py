from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(t) > len(s):
            return ""
        
        # Count the frequency of characters in t
        t_count = Counter(t)
        # This will store the current window character counts
        window_count = {}
        
        # Number of unique characters in t to match
        required = len(t_count)
        # Number of unique characters in the current window that match the frequency in t
        formed = 0
        
        # Pointers for the sliding window
        left, right = 0, 0
        # The smallest window length and the resulting window positions
        min_len = float("inf")
        ans = (0, 0)
        
        while right < len(s):
            # Add the current character to the window count
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If the current character's count in the window matches its count in t
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to shrink the window if all characters from t are in the current window
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if the current window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = (left, right)
                
                # Remove the leftmost character from the window
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                # Move the left pointer to shrink the window
                left += 1
            
            # Move the right pointer to expand the window
            right += 1
        
        # If we found a valid window, return it, otherwise return an empty string
        return "" if min_len == float("inf") else s[ans[0]:ans[1] + 1]
