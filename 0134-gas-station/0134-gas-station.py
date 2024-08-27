class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0
        current_tank = 0
        starting_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            # If current tank is negative, reset the starting station
            if current_tank < 0:
                starting_station = i + 1
                current_tank = 0

        # If total gas is greater than or equal to total cost, return the starting station
        return starting_station if total_tank >= 0 else -1
