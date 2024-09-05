class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initialize two pointers
        i, j = 0, 0
        
        # Iterate through both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer for s
            if s[i] == t[j]:
                i += 1
            # Always move the pointer for t
            j += 1
        
        # If we traversed all of s, it's a subsequence
        return i == len(s)
