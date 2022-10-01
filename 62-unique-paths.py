# Unique Paths
# ----------
# Medium
# Combinatorics

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # for any m x n grid, each unique path requires
        #   N-1 right moves
        #   M-1 down moves
        #   Total = (N-1)+(M-1) = M + N - 2

        return math.comb(m+n-2, m-1)
        # or   math.comb(m+n-2, n-1)