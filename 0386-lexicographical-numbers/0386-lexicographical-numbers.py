class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        current = 1
        
        for _ in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                if current >= n:
                    current //= 10
                current += 1
                while current % 10 == 0:
                    current //= 10
        
        return result
