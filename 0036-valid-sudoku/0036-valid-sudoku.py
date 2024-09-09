class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Use sets to keep track of seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate over each cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.':
                    continue  # Ignore empty cells
                
                # Check row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                # Check column
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                # Check 3x3 sub-box
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        # If no conflicts found, the board is valid
        return True
