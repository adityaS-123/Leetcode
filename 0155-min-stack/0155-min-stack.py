class MinStack(object):

    def __init__(self):
        # Initialize two stacks: one for regular stack operations and one for keeping track of minimums
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # If min_stack is empty or the current value is smaller or equal to the current minimum, push it onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        # Pop from the main stack
        popped_val = self.stack.pop()
        # If the popped value is the same as the top of the min_stack, pop it from the min_stack as well
        if popped_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # Return the top element of the min_stack (which is the current minimum)
        return self.min_stack[-1]
