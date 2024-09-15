class Solution(object):
    def findTheLongestSubstring(self, s):
        # Map vowels to corresponding bits
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Initialize current bitmask and the result
        bitmask = 0
        max_len = 0
        
        # Dictionary to store the first occurrence of each bitmask
        # Start with {0: -1} because an empty prefix means even number of vowels
        bitmask_index = {0: -1}
        
        for i, char in enumerate(s):
            if char in vowel_to_bit:
                # Toggle the corresponding bit for this vowel
                bitmask ^= (1 << vowel_to_bit[char])
            
            # Check if this bitmask has been seen before
            if bitmask in bitmask_index:
                # Calculate the length of the substring
                max_len = max(max_len, i - bitmask_index[bitmask])
            else:
                # Store the first occurrence of this bitmask
                bitmask_index[bitmask] = i
        
        return max_len

        