"""
TODO, write divide and conquer approach
"""

# Brute Force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = nums[0]
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                m = max(m, s)
        return m

    
# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curr = 0
        for i in range(len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
        return best

