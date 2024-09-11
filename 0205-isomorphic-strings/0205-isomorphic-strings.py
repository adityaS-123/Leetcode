class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # Two dictionaries to store the mappings
        map_s_to_t = {}
        map_t_to_s = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check if there's already a mapping for char_s in s
            if char_s in map_s_to_t:
                # If there's a mismatch with the corresponding char in t, return False
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                # Create a new mapping from s to t
                map_s_to_t[char_s] = char_t
            
            # Similarly check if there's a reverse mapping for char_t in t
            if char_t in map_t_to_s:
                # If there's a mismatch with the corresponding char in s, return False
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                # Create a new reverse mapping from t to s
                map_t_to_s[char_t] = char_s
        
        # If all mappings are consistent, the strings are isomorphic
        return True
