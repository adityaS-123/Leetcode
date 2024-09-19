class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        result = 0
        sign = 1  # 1 means positive, -1 means negative
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                current_number = 0
                sign = 1  # Update sign to positive for next operation
            elif char == '-':
                result += sign * current_number
                current_number = 0
                sign = -1  # Update sign to negative for next operation
            elif char == '(':
                # Push the result and sign to the stack for the expression within parentheses
                stack.append(result)
                stack.append(sign)
                result = 0  # Reset result for the expression within parentheses
                sign = 1  # Reset sign for the new sub-expression
            elif char == ')':
                # Calculate the result for the expression inside parentheses
                result += sign * current_number
                current_number = 0
                result *= stack.pop()  # Multiply by the sign before the parentheses
                result += stack.pop()  # Add the result calculated before the parentheses
            elif char == ' ':
                # Skip spaces
                continue
        
        # Add any number left at the end
        result += sign * current_number
        return result
