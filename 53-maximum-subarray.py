# Maximum Subarray
# ----------
# Medium
# Dynamics Programming, Kadanes Algorithm, Greedy

# Dynamic Programming Solution:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)

        for i, num in enumerate(nums):
            dp[i] = max( dp[i-1] + num, num)

        return max(dp)

# Kadane's Solution:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max( num, curr_sum + num)
            max_sum = max( curr_sum, max_sum )
        
        return max_sum