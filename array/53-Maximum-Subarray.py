"""
TODO, write divide and conquer approach
"""


# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curr = 0
        for i in range(len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
        return best

