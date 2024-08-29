class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to their corresponding integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize result
        total = 0
        prev_value = 0
        
        # Iterate over the characters in the Roman numeral string
        for char in s:
            # Get the integer value of the current Roman numeral
            current_value = roman_to_int[char]
            
            # If the previous value is less than the current value, we subtract twice the previous value
            # because we had added it in the previous iteration
            if prev_value < current_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            
            # Update the previous value
            prev_value = current_value
        
        return total
