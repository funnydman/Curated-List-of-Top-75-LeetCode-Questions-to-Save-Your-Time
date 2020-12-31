"""
Some ways to solve:
Approach #1 Sorting [Accepted]
Approach #2 HashSet [Accepted]
Approach #3 Bit Manipulation [Accepted]
Approach #4 Gauss' Formula [Accepted]

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l  = len(nums)
        return l * (l +1)//2 - sum(nums)
        
