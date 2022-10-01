# Longest Common Subsequence
# ----------
# Medium
# 2D Dyanmics Programming, Bottom Up

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # intialise 2D dp array
        t1 = len(text1)
        t2 = len(text2)
        dp = [[0 for j in range(t2 + 1)] for i in range(t1 + 1)]

        # bottom up approach so we are going backwards
        for i in range(t1 - 1, -1, -1):
            for j in range(t2 - 1, -1, -1):
                
                # if characters match, move diagonally
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                
                # else move right or down
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]
