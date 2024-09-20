# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        
        # Traverse the list
        while fast and fast.next:
            # Move slow by one step
            slow = slow.next
            # Move fast by two steps
            fast = fast.next.next
            
            # If they meet, there's a cycle
            if slow == fast:
                return True
        
        # If fast reaches the end, there's no cycle
        return False
