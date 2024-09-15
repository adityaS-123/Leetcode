class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Step 1: Sort the intervals based on the starting value
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the merged intervals list with the first interval
        merged = [intervals[0]]
        
        # Step 3: Iterate through the intervals
        for i in range(1, len(intervals)):
            # Get the last interval in the merged list
            last_interval = merged[-1]
            
            # If the current interval overlaps with the last interval
            if intervals[i][0] <= last_interval[1]:
                # Merge the intervals by updating the end time
                last_interval[1] = max(last_interval[1], intervals[i][1])
            else:
                # If they don't overlap, add the current interval to the merged list
                merged.append(intervals[i])
        
        return merged
