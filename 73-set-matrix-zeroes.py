# Set Matrix Zeroes
# ----------
# Medium
# Matrix

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_array = []

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_array.append([row, col])
        
        for row, col in zero_array:
            for c in range(cols):
                matrix[row][c] = 0
            for r in range(rows):
                matrix[r][col] = 0

        return matrix