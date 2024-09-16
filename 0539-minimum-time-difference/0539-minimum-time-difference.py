class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # Helper function to convert "HH:MM" to minutes
        def timeToMinutes(time):
            h, m = map(int, time.split(':'))
            return h * 60 + m
        
        # Convert all time points to minutes
        minutes = [timeToMinutes(time) for time in timePoints]
        
        # Sort the list of time points in minutes
        minutes.sort()
        
        # Initialize the minimum difference as a large number
        min_diff = float('inf')
        
        # Check differences between consecutive time points
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Check the difference between the last and first time points, accounting for the circular day
        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])
        
        return min_diff
