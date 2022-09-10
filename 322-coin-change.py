Coin Change
# ----------
# Medium
# Dynamic Programming

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # initialise dp array
        # initial array is just a high value check
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # want a dp entry for every amount
        for a in range(1, amount + 1):
            
            # using each coin, find the lowest number usage to total amount
            for coin in coins:
                if (a - coin >= 0):
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
        # tc: O(amount * len(coins))
        # sc: O(amount)        

# https://leetcode.com/problems/coin-change/