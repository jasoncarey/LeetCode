# Maximum Product Subarray
# ----------
# Medium
# Dynamic Programming

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # dp array for max and min
        dp = [nums[0]] * len(nums)        
        mdp = [nums[0]] * len(nums)
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] * dp[i-1], nums[i] * mdp[i-1], nums[i])
            mdp[i] = min(nums[i] * dp[i-1], nums[i] * mdp[i-1], nums[i])
            
        return max(max(dp), max(mdp))
    
# https://leetcode.com/problems/maximum-product-subarray/