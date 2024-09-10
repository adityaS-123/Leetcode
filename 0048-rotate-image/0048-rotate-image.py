class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

# Example usage:
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix1)
print(matrix1)  # Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix2)
print(matrix2)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
