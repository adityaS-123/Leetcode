class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Take the first string as the reference
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Update the prefix until it matches the start of each string
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Shorten the prefix
                if not prefix:
                    return ""  # No common prefix
        
        return prefix

# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))  # Output: ""
