class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Memoization to store intermediate results
        memo = {}
        
        # Helper function to compute all results
        def compute_ways(expr):
            # If the result is already in memo, return it
            if expr in memo:
                return memo[expr]
            
            results = []
            # Iterate through the expression
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    # Split into left and right subexpressions
                    left_expr = expr[:i]
                    right_expr = expr[i+1:]
                    
                    # Recursively compute results for left and right parts
                    left_results = compute_ways(left_expr)
                    right_results = compute_ways(right_expr)
                    
                    # Combine results using the current operator
                    for left in left_results:
                        for right in right_results:
                            if expr[i] == '+':
                                results.append(left + right)
                            elif expr[i] == '-':
                                results.append(left - right)
                            elif expr[i] == '*':
                                results.append(left * right)
            
            # If no operator found, the expression is a single number
            if not results:
                results.append(int(expr))
            
            # Memoize and return the result
            memo[expr] = results
            return results
        
        # Call the helper function
        return compute_ways(expression)
