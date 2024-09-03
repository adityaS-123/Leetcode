class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Step 1: Handle the edge case where numRows is 1
        if numRows == 1:
            return s
        
        # Step 2: Initialize a list with an empty string for each row
        rows = [''] * min(numRows, len(s))
        
        # Step 3: Iterate through the characters in the string
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            # Step 4: Change direction when reaching top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        # Step 5: Join all rows together to form the final string
        return ''.join(rows)
